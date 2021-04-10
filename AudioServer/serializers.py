from rest_framework import serializers
from .models import *

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'uploadTime']
class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    #id = serializers.IntegerField(max_value = None, min_value = 0)
    #name = serializers.CharField(max_length=100)
    #uploadTime = serializers.DateTimeField()
    #host = serializers.CharField(max_length=100)
    #participants = serializers.RelatedField(many=True)
   class Meta:
       model = Podcast
       fields = ['id', 'name', 'duration', 'uploadTime', 'host', 'participants']
class AudioBookSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField(max_value = None, min_value = 0)
    # title = serializers.CharField(max_length=100)
    # author = serializers.CharField(max_length=100)
    # narrator = serializers.CharField(max_length=100)
    # duration = serializers.IntegerField(max_value = None, min_value = 0)
    # uploadTime = serializers.DateTimeField(auto_now=True)
   class Meta:
       model = AudioBook
       fields = ['id', 'title', 'author', 'narrator', 'duration', 'uploadTime']

class PodcastParticipantSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField(max_value = None, min_value = 0)
    # name = serializers.CharField(max_length=100)
   class Meta:
       model = PodcastParticipant
       fields = ['id', 'name']
