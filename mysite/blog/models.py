from django.conf import settings
from django.utils import timezone
from django.db import models
#import string
#import random
from django.urls import reverse


# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    published = models.DateTimeField('Опубликован', auto_now_add=True)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='file_txt')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    file = models.FileField(upload_to='file/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name




# class PostFile(models.Model):
#     title = models.TextField()
#     cover = models.FileField(upload_to='file/')
#
#     def __str__(self):
#         return self.title
#
#
# class File(models.Model):
#     slug = models.SlugField(max_length=10, primary_key=True, blank=True)
#     file = models.FileField(upload_to='file/')
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = ''.join(random.sample(string.ascii_lowercase, 6))
#         super(File, self).save(*args, **kwargs)
#
#     def get_absolute_url(self):
#         return reverse('file_detail', args=(self.slug,))
