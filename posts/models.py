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

from user_profile.models import User


class Post(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=30, default='Global')
    is_active = models.BooleanField(default=True)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.text[:50]



