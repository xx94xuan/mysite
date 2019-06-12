from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Picture
from .forms import GalleryForm

# Create your views here.
def index(request):
    # return HttpResponse("hello gallery.")
    imgs = Picture.objects.all()
    return render(request, 'gallery/index.html', {'imgs': imgs})

def new(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            new_pic = Picture()
            new_pic.img_alt = form.cleaned_data['img_alt']
            new_pic.img_author = form.cleaned_data['img_author']
            new_pic.save()

            # 'GalleryForm' object has no attribute 'save' ???
            # form.save()
            return HttpResponseRedirect('/gallery/')
    else: 
        form = GalleryForm()

    # return render(request, 'texting/index.html', {'form': form})
    return render(request, 'gallery/new.html', {'form': form})

def show(request, picture_id):
    pic = get_object_or_404(Picture, pk=picture_id)
    context = {
        'pic': pic
    }
    return render(request, 'gallery/show.html', context)