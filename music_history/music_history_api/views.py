from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history import serializers, models

class UserViewSet(viewsets.ModelViewSet):
    """
    This creates the User view
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    """
    This creates the Artist view
    """
    queryset = Artist.objects.all()
    serializer_class = serializers.ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    This creates the Album view
    """
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    This creates the Genre view
    """
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class SongViewSet(viewsets.ModelViewSet):
    """
    This creates the Song view
    """
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer




