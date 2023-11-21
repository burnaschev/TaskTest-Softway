from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(max_length=250, **NULLABLE, verbose_name='описание')
    status = models.BooleanField(default=False, verbose_name='статус')
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата создания')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Пользователь')

    def __str__(self):
        return f"{self.title} ({self.description})"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
