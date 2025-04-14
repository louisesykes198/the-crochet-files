# crochet_app/urls.py
from django.urls import path
from . import views
from .views import CustomLoginView
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
      # URL to view a project and its comments
    path('project/<int:project_id>/comment/', views.add_comment, name='add_comment'),

    # URL to add a comment to a project
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    
    # Like Button
    path('project/<int:project_id>/like/', views.toggle_like, name='toggle_like'),
    
    # project form
    path('project/new/', views.create_project, name='create_project'),
    
    path('patterns/', views.pattern_list, name='pattern_list'),
    path('patterns/<int:pk>/', views.pattern_detail, name='pattern_detail'),
    
    path('login/', CustomLoginView.as_view(), name='login'),
    
    path('register/', register, name='register'),
    
    path('projects/<int:pk>/edit/', views.update_project, name='update_project'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/', views.project_list, name='project_list'),
    path('add/', views.add_project, name='add_project'),
]


#from django.urls import path
#from . import views

#urlpatterns = [
    #path('', views.CrochetList.as_view(), name='home'),  # class-based view
#]
