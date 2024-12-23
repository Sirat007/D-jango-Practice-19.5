from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class MusicianModel(models.Model):
    instruments = (
        ('cello','cello'),
        ('gitar','gitar'),
        ('flute','flute'),
    )
    first_name = models.CharField(max_length=40,default=None)
    last_name = models.CharField(max_length=40,default=None)
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=11)
    instrument_type = models.CharField(max_length=20,choices=instruments)

    def __str__(self):
        return self.first_name