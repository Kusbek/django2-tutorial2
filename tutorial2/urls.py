from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import product.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product.views.homepage, name = 'homepage'),
    path('account/', include('account.urls')),
    path('product/', include('product.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
