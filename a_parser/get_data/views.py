from django.shortcuts import render, redirect


import requests as req
import re

from .models import LogsModel

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
pattern = re.compile(r'\s+'.join(PARTS)+r'\s*\Z')

def home_page(request):
    return render(request, 'index.html', {})


def get_and_save_data(request):
    url = request.POST['content']
    data = req.get(url)
    data = data.text.strip().split('\n')

    for line in data:
        new_logs = LogsModel()
        matching = pattern.match(line)
        info = matching.groupdict()
        
        new_logs.ip = info['host']
        new_logs.data = info['time']
        new_logs.method = info['request'].split()[0]
        new_logs.url = info['request'].split()[1]
        new_logs.response = info['status']

        try:
            new_logs.response_size = int(info['size'])
        except ValueError:
            new_logs.response_size = 0

        new_logs.save()
    
    return redirect('home-page')

