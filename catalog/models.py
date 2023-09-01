from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='catalog/', verbose_name='превью', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    purchase_price = models.IntegerField(verbose_name='цена')
    creation_data = models.DateField(verbose_name='дата создания')
    last_modified = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.purchase_price})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='категория')
    category_description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
