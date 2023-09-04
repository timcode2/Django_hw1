import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {
                "name": "Робот",
                "description": "Это просто Киборг, без комментариев",
                "category": 1,
                "purchase_price": 1000000,
                "creation_data": "2021-04-22"
            },
            {
                "name": "Гитара",
                "description": "Нейлоновые струны и классическое звучание",
                "category": 3,
                "purchase_price": 6700,
                "creation_data": "2023-07-26"
            },
            {
                "name": "Подшипник",
                "description": "Надёжная работа",
                "category": 2,
                "purchase_price": 1500,
                "creation_data": "2023-08-29"
            }]

        category_list = [{
            "category_name": "Электроника",
            "category_description": "Список электротехники"
            },
            {
                "category_name": "Запчасти",
                "category_description": "Список запчастей для техники"
            },
            {
                "category_name": "Музыкальные инструменты",
                "category_description": "Каталог музыкальных инструментов"
            }]

        for product in product_list:
            Product.objects.create(**product)

        for category in category_list:
            Category.objects.create(**category)