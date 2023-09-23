from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index_contact, ProductListView, ProductDetailsView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', index_contact, name='contact'),
    path('product/<int:pk>', ProductDetailsView.as_view(), name='product'),
]
