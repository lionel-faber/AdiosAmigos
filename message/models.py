from django.db import models

class List(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Bubye(models.Model):
    recv = models.CharField(max_length=50)
    text = models.CharField(max_length=5000)
    def __str__(self):
        return self.text
