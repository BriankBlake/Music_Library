from rest_framework import serializers
from music.models import Music


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ["id", "title", "artist", "album", "release_date", "genre"]
