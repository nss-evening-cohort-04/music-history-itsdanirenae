from django.contrib.auth.models import User
from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    year_established = models.DateField()


    class Meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return '{}'.format(self.artist_name)

