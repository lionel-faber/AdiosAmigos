from django.db import models
from django.contrib.auth.models import User


class Bubye(models.Model):
    alumini = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField(max_length=5000)
    # def __str__(self):
    #     return 'message of {}--- {}'.format(self.alumini.username,self.message)
