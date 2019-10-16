from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name = 'create'),
    path('<int:prod_id>/', views.detail, name = 'detail'),
    path('<int:prod_id>/upvote/', views.upvote, name = 'upvote'),
]