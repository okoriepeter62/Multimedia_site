from django.shortcuts import render, redirect, get_object_or_404
from .models import Media
from .forms import MediaForm


def home(request):
    media = Media.objects.all()
    return render(request, 'home.html', {'media': media})


def upload(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # IMPORTANT FIX
    else:
        form = MediaForm()

    return render(request, 'upload.html', {'form': form})


def edit_media(request, id):
    media = get_object_or_404(Media, id=id)

    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES, instance=media)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MediaForm(instance=media)

    return render(request, 'upload.html', {'form': form})


def delete_media(request, id):
    media = get_object_or_404(Media, id=id)
    media.delete()
    return redirect('home')
