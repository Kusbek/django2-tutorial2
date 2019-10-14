from django.contrib import admin
from django.urls import path
from django.conf import settings
import product.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product.views.homepage, name = 'homepage'),
]
