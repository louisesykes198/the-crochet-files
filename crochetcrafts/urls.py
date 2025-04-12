from django.contrib import admin
from django.urls import path, include  # include is important here

urlpatterns = [
    path('admin/', admin.site.urls),           # Admin panel
    path('', include('crochet_app.urls')),     # Your app's URLs
]
