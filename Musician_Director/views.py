from django.shortcuts import render,redirect
from album.models import AlbumModel
from musician.models import MusicianModel


def home(request):
    
    data = AlbumModel.objects.all()
    return render(request, 'home.html',{'data':data})

