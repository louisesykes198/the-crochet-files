from django.urls import path
from . import views
from .views import register
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    # Home view
    path('', views.home, name='home'),

    # Project list, add, edit, delete
    path('projects/', views.project_list, name='project_list'),
    path('project/new/', views.add_project, name='add_project'),
    path('project/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),

    # Project detail, comment, like
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/comment/', views.add_comment, name='add_comment'),
    path('project/<int:project_id>/like/', views.toggle_like, name='toggle_like'),

    # Category-based filtering
    path('category/<str:category_name>/', views.category_view, name='category_view'),

    # Auth
    path('register/', register, name='register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

