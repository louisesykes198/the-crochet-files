from django.contrib import admin
from django.urls import path, include  # include is important here

urlpatterns = [
    path('admin/', admin.site.urls),           # Admin panel
    path('summernote/', include('django_summernote.urls')),
    path('', include('crochet_app.urls')),     # Your app's URLs
]
