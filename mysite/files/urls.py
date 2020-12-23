# -*- coding: utf-8 -*-
from django.urls import path
from .views import UploadView
from .views import my_view
# from .views import FileFieldView
urlpatterns = [
    path('files2/', UploadView.as_view(), name='UploadView'),
    path('files/', my_view, name='my-view'),
    # path('files/', FileFieldView.as_view(), name='FileFieldView')
    # path('files/', FileFieldView.as_view(), name='FileFieldView')
]
