"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls')),
#     url('', include('blog.urls')),
#     url(r'^images/', include(('images.urls', 'images'), namespace='images')),
# ]
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from files import views as uploader_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('loggers.urls')),
    path('', include('blog.urls')),
    url('', include('blog.urls')),
#    url(r'^images/', include(('images.urls', 'images'), namespace='images')),
    path('', uploader_views.UploadView.as_view(), name='fileupload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    path('info/', list_post2),
#    path('lib/', list_post3),
