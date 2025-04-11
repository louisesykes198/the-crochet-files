# crochetcraft/urls.py
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.index, name='craft_index'),  # Homepage or list view for crochet crafts
    path('craft/<int:id>/', views.craft_detail, name='craft_detail'),  # View for individual crochet crafts
    path('add/', views.add_craft, name='add_craft'),  # Add new crochet craft
]
