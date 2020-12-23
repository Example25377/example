# -*- coding: utf-8 -*-
from django import forms

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class DocumentForm(forms.Form):
    docfile = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),label='Select a file')




