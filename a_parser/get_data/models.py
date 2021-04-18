from django.db import models

#создаем таблицу по заданию
class LogsModel(models.Model):
    ip = models.GenericIPAddressField()
    date = models.CharField(max_length=30)
    method = models.CharField(max_length=4)
    url = models.TextField()
    response = models.IntegerField()
    response_size = models.IntegerField()

    #добавляем, чтобы можно было вывести данные в консоле в читаемом виде
    def __str__(self):
        return f'{self.ip}, {self.date}'