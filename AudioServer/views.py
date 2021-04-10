from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
# Create your views here.

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer
class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all().order_by('id')
    serializer_class = PodcastSerializer
class AudioBookViewSet(viewsets.ModelViewSet):
    queryset = AudioBook.objects.all().order_by('id')
    serializer_class = AudioBookSerializer
class PodcastParticipantViewSet(viewsets.ModelViewSet):
    queryset = PodcastParticipant.objects.all().order_by('id')
    serializer_class = PodcastParticipantSerializer
