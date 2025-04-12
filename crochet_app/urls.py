from django.urls import path
from .views import project_list

urlpatterns = [
    path('', project_list, name='project_list'),
]


#from django.urls import path
#from . import views

#urlpatterns = [
    #path('', views.CrochetList.as_view(), name='home'),  # class-based view
#]
