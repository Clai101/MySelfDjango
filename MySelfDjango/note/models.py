from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Заголовок')
    desription =  models.TextField(null = True, verbose_name = 'Описание')
    another_information = models.CharField(max_length = 255, verbose_name = 'Другая иформация')
    date = models.TextField(null = True, verbose_name = 'Дата публикации')
    image = models.ImageField(verbose_name = 'Картинка продукта')
    link = models.TextField(null = True, verbose_name = 'Сылка')
    orign = models.TextField(null = True, verbose_name = 'Источник')
    def  __str__(self):
        return self.desription