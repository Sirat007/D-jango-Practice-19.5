from django.db import models
from musician.models import MusicianModel

# Create your models here.

class AlbumModel(models.Model):
    rating = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    )
    album_name = models.TextField()
    musician = models.ForeignKey(MusicianModel,on_delete=models.CASCADE,null=True,blank=True)
    release_date = models.DateField()
    rating = models.IntegerField(choices=rating)

    def __str__(self):
        return self.musician.first_name
    