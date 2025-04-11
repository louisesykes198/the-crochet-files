# crochet_app/urls.py
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage or list view for crochet items
    path('item/<int:id>/', views.item_detail, name='item_detail'),  # View for individual crochet items
    path('add/', views.add_item, name='add_item'),  # Add new crochet item
]
