from django import forms
from .models import AlbumModel

class Album_Form(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'