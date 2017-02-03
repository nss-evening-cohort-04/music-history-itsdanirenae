from django.contrib.auth.models import User
from rest_framework import serializers
from music_history_api import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Explixitly creates a User serializer
    """
    class Meta:
        model = User
        fields = ('first_name',)


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    This is the hyperlinked serailizer for the Artist Model
    """
    class Meta:
        model = models.Artist
        fields = '__all__'


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """
    This is the hyperlinked serailizer for the Album Model
    """
    class Meta:
        model = models.Album
        fields = '__all__'


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    This is the hyperlinked serailizer for the Genre Model
    """
    class Meta:
        model = models.Genre
        fields = '__all__'


class SongSerializer(serializers.HyperlinkedModelSerializer):
    """
    This is the hyperlinked serailizer for the Song Model
    """
    class Meta:
        model = models.Song
        fields = '__all__'



