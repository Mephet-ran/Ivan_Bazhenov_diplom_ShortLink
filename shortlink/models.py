from django.db import models
from django.contrib.auth.models import User


class ShortLink(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    link = models.URLField('Ссылка', max_length=250)
    word = models.CharField('Слово', max_length=20, unique=True)


    def __str__(self):
        return f'ShortLink пользователя {self.user.username} для слова {self.word}'
