from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='категория')
    category_description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='catalog/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', **NULLABLE)
    purchase_price = models.IntegerField(verbose_name='цена')
    creation_data = models.DateField(verbose_name='дата создания')
    last_modified = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                verbose_name='создатель')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')

    version_number = models.IntegerField(default=1, verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='активная версия')

    def __str__(self):
        return f'{self.product} (ver. {self.version_number})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

