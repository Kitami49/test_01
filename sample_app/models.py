from django.db import models

# Create your models here.
# class Post(models.Model):
#     name = models.CharField('user name', max_length=15)
#     micropost = models.CharField('tweet', max_length=140, blank=True)

#     def __str__(self):
#         return self.name


class Post(models.Model):
    #id = models.IntegerField('user id', primary_key=True)
    name = models.CharField('名前', max_length=15)
    micropost = models.IntegerField('年齢', blank=True)

    def __str__(self):
        return self.name


class Calc(models.Model):
    num1 = models.IntegerField('num1', blank=False)
    num2 = models.IntegerField('num2', blank=False)
    
    # sum = models.IntegerField('加', blank=True)
    # sub = models.IntegerField('減', blank=True)
    # mul = models.IntegerField('乗', blank=True)
    # div = models.IntegerField('除', blank=True)