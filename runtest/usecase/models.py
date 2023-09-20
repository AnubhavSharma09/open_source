from django.db import models

# Create your models here.


class xVariable(models.Model):
    X = models.IntegerField(verbose_name='Value',default=0)
   


class Yvariable(models.Model):
    question = models.ForeignKey(xVariable, on_delete=models.CASCADE)
    Y = models.IntegerField(verbose_name='Value',default=0)
   