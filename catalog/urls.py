from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index_contact, ProductListView, ProductDetailsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', index_contact, name='contact'),
    path('product/<int:pk>', ProductDetailsView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
