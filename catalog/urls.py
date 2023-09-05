from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index_home, index_contact, index_product

urlpatterns = [
    path('', index_home, name='home'),
    path('contacts/', index_contact, name='contact'),
    path('product/<int:pk>', index_product, name='product'),
]
