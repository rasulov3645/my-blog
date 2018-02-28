from django.db import models

# Create your models here.

'''
link:   https://djbook.ru/rel1.9/ref/models/fields.html

# Небольшой справочник
1) IntegerField     - Целое число
2) TextField        - Поле для большего текста
3) DateTimeField    - Поле дата-время
4) EmailField       - Поле для электронной почты. 
5) URLField         - Поле для URK-адреса
6) FileField        - Поле загружаемого файла.

'''



"""
# Отношение многие-к-одному
class School(models.Model):
    pass

class Student(models.Model):
    school = models.ForeignKey(School)


# Отношение один-к-одному
class Entry(models.Model):
    pass

class EnttyDetail(models.Model):
    entry = models.OneToOneField(Entry)
    details = models.TextField()


# Отношение многие-ко-многим
class Product(models.Model):
    name = models.CharField()

class Category(models.Model):
    name = models.CharField(
        product = models.ManyToManyField('Product', blank=True, null=True),
    )
"""