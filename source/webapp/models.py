from django.db import models
from django.db.models import TextChoices


# Create your models here.

class StatusChoice(TextChoices):
    ACTIVE = 'active', 'Активно'
    BLOCKED = 'blocked', 'Заблокировано'


class GuestBook(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя гостя')
    email = models.EmailField(max_length=100, null=False, blank=False, verbose_name='EMAIL гостя')
    text = models.TextField(max_length=1000, null=True, blank=False, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время")
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.ACTIVE,
                              verbose_name='Статус')

    def __str__(self):
        return f'{self.name} | {self.email}'
