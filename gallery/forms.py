from django import forms
from .models import *

class GalleryForm(forms.ModelForm):
    # img = forms.ImageField()
    # img_alt = forms.CharField(label='alt',max_length=200)
    # img_author = forms.CharField(label='author', max_length=100)

    class Meta:
        model = Picture
        fields = ['img', 'img_alt', 'img_author']
