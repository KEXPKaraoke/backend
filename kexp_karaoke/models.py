from django.db import models

# Create your models here.

class NowPlaying(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    time_on_air = models.TimeField()
    lyrics = models.TextField()

    def __str__(self):
        return self.title
