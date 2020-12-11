"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from .views import PostDetail, PostList
from . import views

app_name = 'blog'


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post'),
    path('', PostList.as_view(), name='index'),
    path('home/', views.post_list, name='post_list_1'),
    path(r'info/', views.post_list2, name='post_list2'),
    path(r'lib/', views.post_list3, name='post_list3'),
    path(r'gif/', views.gif, name='gif'),
#    url(r'^(?P<slug>[-\w\d\_]+)/$', FileDetailView.as_view(),name='file_detail'),
]
