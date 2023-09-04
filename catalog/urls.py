from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import home, contact


urlpatterns = [
    path('', home),
    path('contacts/', contact)
]