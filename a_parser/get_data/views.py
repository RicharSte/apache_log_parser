from django.shortcuts import render, redirect

import requests as req
import re

from .models import LogsModel

#Добавляем параметры для регулярный выражений
PARTS = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]

#Объединяем все в ежино
pattern = re.compile(r'\s+'.join(PARTS)+r'\s*\Z')

#рендерим основную страницу
def home_page(request):
    return render(request, 'index.html', {})

#получаем данные из ссылки на лог
def get_and_save_data(request):
    url = request.POST['content'] #Получаем url с сайта
    if url[-3:] == 'log': #проверяем, является ли файл логовым
        data = req.get(url) #берём даннык из ссылки
        data = data.text.strip().split('\n') #разделяем его на отдельные линии
                                             #каждая линия-новый запрос
        #проходимся по данным
        for line in data: #
            new_logs = LogsModel() #создаем элемент таблицы, для каждого элемента
            matching = pattern.match(line) #применяем паттерн
            info = matching.groupdict() #формируем словарь с уже "очищенными данными"
            
            #метим данные
            new_logs.ip = info['host']
            new_logs.date = info['time']
            new_logs.method = info['request'].split()[0]
            new_logs.url = info['request'].split()[1]
            new_logs.response = info['status']

            #иногда в логах нет размера, тогда мы заменяем это на 0
            try:
                new_logs.response_size = int(info['size'])
            except ValueError:
                new_logs.response_size = 0

            #сохраняем даннык
            new_logs.save()
    
    #перенаправляем пользователя обратно на главную (очищаем поле импута)
    return redirect('home-page')