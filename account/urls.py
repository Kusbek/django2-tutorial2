from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name = 'account'),
    path('signup', views.signup, name = 'signup'),
    path('login', views.login, name = 'login')
]