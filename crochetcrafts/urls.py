# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crochet_app.urls')),  # Add other app URL patterns here
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#rom django.contrib import admin
#from django.urls import path, include  # include is important here

#urlpatterns = [
    #path('admin/', admin.site.urls),           # Admin panel
    #path('summernote/', include('django_summernote.urls')),
    #path('', include('crochet_app.urls')),     # Your app's URLs
#]
