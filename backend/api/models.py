# Create your models here.
# api/models.py
from django.db import models

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100, null=True, default=None)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100, null=True, blank=True)  		# field for album
    duration = models.IntegerField(null=True, blank=True)  					# field for duration
    spotify_id = models.CharField(max_length=100, null=True, blank=True)  	# field for Spotify ID
    #audio_file = models.FileField(upload_to='audio/') # original with problem. The project use the Spotify's URL! solution below.
    #audio_img = models.FileField(upload_to='audio_img/') # original with problem. The project use the Spotify's URL! solution below.
    audio_file = models.URLField()  # solution for using Spotify's url!
    audio_img = models.URLField()   # solution for using Spotify's url!

    def __str__(self):
        return self.title