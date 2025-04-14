# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crochet_app.urls')),  # Only include this once
    path('accounts/', include('django.contrib.auth.urls')),  # For login, logout, and password reset
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development



#rom django.contrib import admin
#from django.urls import path, include  # include is important here

#urlpatterns = [
    #path('admin/', admin.site.urls),           # Admin panel
    #path('summernote/', include('django_summernote.urls')),
    #path('', include('crochet_app.urls')),     # Your app's URLs
#]
