from django.shortcuts import render
from django.views.generic import DetailView, ListView

from catalog.models import Product


# def index_home(request):
#     product = Product.objects.all()
#     context = {
#         'object_list': product
#     }
#     return render(request, "catalog/product_list.html", context)
class ProductListView(ListView):
    model = Product


def index_contact(request):
    return render(request, "catalog/contact_page.html")


class ProductDetailsView(DetailView):
    model = Product


# def index_product(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {
#         'object': product,
#         'title': f'Товар - {product.name}'
#     }
#     return render(request, "catalog/product_detail.html", context)
