from rest_framework import serializers
from .models import NowPlaying

class NowPlayingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NowPlaying
        fields = ('id', 'title', 'artist', 'time_on_air', 'lyrics')
