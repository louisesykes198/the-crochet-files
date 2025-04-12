from django.urls import path
from . import views

urlpatterns = [
    path('', views.CrochetList.as_view(), name='home'),  # class-based view
]
