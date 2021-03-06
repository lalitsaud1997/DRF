from .models import Singer, Song
from rest_framework import serializers



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','album','singer','duration']


class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='album')
    #song = serializers.HyperlinkedIdentityField(view_name='song-detail')
    #for nested serializer...
    song = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id','name','gender','artist','song']