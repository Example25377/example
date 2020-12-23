from django.db import models


class Upload(models.Model):
    upload_file = models.FileField(upload_to='documents/%Y/%m/%d')
    upload_date = models.DateTimeField(auto_now_add=True)



class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
