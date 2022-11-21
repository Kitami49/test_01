from django.db import models

class Post(models.Model):
    name = models.CharField('名前', max_length=15)
    micropost = models.IntegerField('年齢', blank=True)

    def __str__(self):
        return self.name


class Calc(models.Model):
    num1 = models.IntegerField('num1', blank=False)
    num2 = models.IntegerField('num2', blank=False)