from django.shortcuts import render
from django.views.generic import DetailView, ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


def index_contact(request):
    return render(request, "catalog/contact_page.html")


class ProductDetailsView(DetailView):
    model = Product
