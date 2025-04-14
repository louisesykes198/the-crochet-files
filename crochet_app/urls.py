from django.urls import path
from . import views
from .views import CustomLoginView
from .views import register
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Home view
    path('', views.home, name='home'),

    # Project Detail and Comments
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/comment/', views.add_comment, name='add_comment'),

    # Like Button
    path('project/<int:project_id>/like/', views.toggle_like, name='toggle_like'),

    # Project CRUD
    path('project/new/', views.add_project, name='add_project'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/', views.project_list, name='project_list'),

    # User Authentication
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    
    path('project/<int:project_id>/like/', views.toggle_like, name='toggle_like'),

    # Static files (for media, if used)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#from django.urls import path
#from . import views

#urlpatterns = [
    #path('', views.CrochetList.as_view(), name='home'),  # class-based view
#]
