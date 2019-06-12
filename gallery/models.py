from django.db import models

# Create your models here.
class Picture(models.Model):
    img = models.ImageField(upload_to='images/')
    img_alt = models.CharField(max_length=200)
    img_author = models.CharField(max_length=100)
