from django.db import models

from datetime import datetime

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=200, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='images/previews', verbose_name='Превью', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='Дата создания', default=datetime.now())
    is_published = models.BooleanField(verbose_name='Опубликован ли', default=True)
    views_counter = models.IntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
