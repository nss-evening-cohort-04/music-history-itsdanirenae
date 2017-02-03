from django.contrib.auth.models import User
from django.db import models



class Artist(models.Model):
  artist_name = models.CharField(max_length=200)
  year_established = models.DateField()

  class Meta:
    verbose_name_plural = 'Artists'

  def __str__(self):
    return '{}'.format(self.artist_name)


class Genre(models.Model):
  genre_label = models.CharField(max_length=200)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'Genre'

  def __str__(self):
    return '{}'.format(self.genre_label)


class Album(models.Model):
  album_title = models.CharField(max_length=200)
  release_date = models.DateField()
  album_duration = models.DateTimeField()
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'Genre'

  def __str__(self):
    return '{} {}'.format(self.album_title, self.artist)


class Song(models.Model):
  song_title = models.CharField(max_length=200)
  song_duration = models.DateTimeField()
  artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = 'Songs'

  def __str__(self):
    return '{} {} {}'.format(self.song_title, self.artist_name, self.album)



