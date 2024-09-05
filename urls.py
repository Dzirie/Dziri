
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('picture/',include('picture.urls')),
    #path('',include('django.contrib.auth.urls')),
    path('my_files/',include('my_files.urls')),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
