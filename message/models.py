from django.db import models

class List(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Bubye(models.Model):
    alumini = models.ForeignKey(List,on_delete=models.CASCADE)
    message = models.TextField(max_length=5000)
    def __str__(self):
        return 'message of {}--- {}'.format(self.alumini.name,self.message)
