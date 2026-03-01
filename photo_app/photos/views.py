from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm, RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photos/photo_list.html', {'photos': photos})

def order_photos_by_name(request):
    photos = Photo.objects.all().order_by(Lower('name'))
    return render(request, 'photos/photo_list.html', {'photos': photos})

def order_photos_by_date(request):
    photos = Photo.objects.all().order_by('upload_date')
    return render(request, 'photos/photo_list.html', {'photos': photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photos/photo_detail.html', {'photo': photo})

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'photos/upload_photo.html', {'form': form})

@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if photo.user == request.user:
        photo.delete()
    return redirect('photo_list')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('photo_list')
    else:
        form = RegisterForm()
    return render(request, 'photos/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('photo_list')