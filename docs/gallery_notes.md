# Notes while setting up Gallery

## Build the Basic Frame

+ `python manage.py startapp gallery`

## Website Feature
Description:
1. Visit "/gallery", there has a linkout to create a new image, all the images' alt will show on the below.
2. On "/gallery/new", there is a form with 3 fields(img, img_alt, img_author) to fill in and a button to submit the form.
3. After submit the image just created by the second step, the page will redirect to the "/gallery" page, and the new image's alt text will show at the end.
4. Click on the alt text, it will link to "/gallery/PICTURE_ID" and show the details of the image(image, alt and author).

## Start on

+ In gallery/models.py, create a model named 'Picture' with 3 fields: img, img_alt and img_author.

    ```
    from django.db import models

    class Picture(models.Model):
        # upload_to config the place the uploaded images stored, this is related to the MEDIA_ROOT configured on urls.py
        img = models.ImageField(upload_to='images/')
        img_alt = models.CharField(max_length=200)
        img_author = models.CharField(max_length=100)
    ```

+ Create views.
In views.py,
1. import the Picture model and create the 'index' view to send all the images to 'template/gallery/index.html'
    ```
    from .models import Picture

    def index(request):
        imgs = Picture.objects.all()
        return render(request, 'gallery/index.html', {'imgs': imgs})
    ```

2. create the 'new' view to get the form data, saved the form and redirect to 'template/gallery/index.html'
.html', {'form': form})
    ``````
    def new(request):
        if request.method == 'POST':

            # GalleryForm will be provided after
            form = GalleryForm(request.POST, request.FILES)
            if form.is_valid():
                form.cleaned_data
                form.save()
                return HttpResponseRedirect('/gallery/')
        else: 
            form = GalleryForm()

        return render(request, 'gallery/new.html',  {'form': form})
    ```

3. create the 'show' view to get the image by id and show the image by 'template/gallery/show.html'
    ```
    def show(request, picture_id):
        pic = get_object_or_404(Picture, pk=picture_id)
        context = {
            'pic': pic
        }
        return render(request, 'gallery/show.html', context)
    ```

### GalleryForm
Create a form from models, create 'gallery/forms.py'

```
from .models import *

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['img', 'img_alt', 'img_author']
```


4. To allow getting the uploaded images by relative path
    1. In mysite/settings.py, add the following code
    ```
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
    MEDIA_URL = '/media/'
    ```
    
    2. In mysite/urls.py, add the following code

    ```
    from django.conf import settings 
    from django.conf.urls.static import static

    if settings.DEBUG:
        # a folder named 'media' root path will be created while images uploaded
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
5. Completed the [templates](https://github.com/xx94xuan/mysite/tree/master/gallery/templates/gallery)

    _NOTEs_: `enctype="multipart/form-data` is significant in the `<form>` tag

## docker image for Gallery app
`docker pull dockerforxxx/xxx-app:9aefc64ceef1a03ae577ee5beed71db642463487`