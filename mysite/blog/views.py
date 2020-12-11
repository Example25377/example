from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse
from django.db import models


# class FileView(DetailView):
#     model = FileDetailView
#
# class MyModel(models.Model):
#     slug = models.SlugField()


def post_list(request):
    return render(request, 'blog/post_list_1.html', {})

def post_list2(request):
    return render(request, 'blog/post_list2.html', {})

def post_list3(request):
    return render(request, 'blog/post_list3.html', {})

def gif(request):
    return render(request, 'blog/gif.html', {})


from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from analytics.decorators import counted
from .models import Post


class PostList(ListView):
    model = Post


@method_decorator(counted, name='dispatch')
class PostDetail(DetailView):
    model = Post