from django.db import models

class LogsModel(models.Model):
    ip = models.GenericIPAddressField()
    data = models.CharField(max_length=30)
    method = models.CharField(max_length=4)
    url = models.TextField()
    response = models.IntegerField()
    response_size = models.IntegerField()
