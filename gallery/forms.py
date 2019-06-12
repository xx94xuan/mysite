from django import forms

class GalleryForm(forms.Form):
    img_alt = forms.CharField(label='alt',max_length=200)
    img_author = forms.CharField(label='author', max_length=100)
