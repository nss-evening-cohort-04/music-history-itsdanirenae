from django.contrib.auth.models import
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
  """
  Explixitly creates a User serializer
  """
    class Meta:
        model = User
        fields = '__all__'


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
  """
  This is the hyperlinked serailizer for the Artist Model
  """
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
  """
  This is the hyperlinked serailizer for the Album Model
  """
    class Meta:
        model = Album
        fields = '__all__'


class GenreSerializer(serializers.HyperlinkedModelSerializer):
  """
  This is the hyperlinked serailizer for the Genre Model
  """
    class Meta:
        model = Genre
        fields = '__all__'


class SongSerializer(serializers.HyperlinkedModelSerializer):
  """
  This is the hyperlinked serailizer for the Song Model
  """
    class Meta:
        model = Song
        fields = '__all__'



