import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('catalog_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        product_list = []
        category_list = []

        for d in data:
            d.pop('pk')
            if d['model'] == 'catalog.product':
                product_list.append(d)
            else:
                category_list.append(d)

        Product.objects.bulk_create(product_list)
        Category.objects.bulk_create(category_list)



