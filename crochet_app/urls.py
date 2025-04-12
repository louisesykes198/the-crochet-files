# crochet_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add more URL patterns as needed
]


#from django.urls import path
#from . import views

#urlpatterns = [
    #path('', views.CrochetList.as_view(), name='home'),  # class-based view
#]
