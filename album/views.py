from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import models,forms

# Create your views here.

@method_decorator(login_required,name='dispatch')
class AddAlbum(CreateView):
    model = models.AlbumModel
    form_class = forms.Album_Form
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required,name='dispatch')
class EditAlbum(UpdateView):
    model = models.AlbumModel
    form_class = forms.Album_Form
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')