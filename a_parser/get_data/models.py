from django.db import models

class LogsModel(models.Model):
    ip = models.GenericIPAddressField()
    date = models.CharField(max_length=30)
    method = models.CharField(max_length=4)
    url = models.TextField()
    response = models.IntegerField()
    response_size = models.IntegerField()

    def __str__(self):
        return f'{self.ip}, {self.date}'