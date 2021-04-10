from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'songs', SongView, basename="Songs")
router.register(r'audiobook',AudioBookViewSet)
router.register(r'podcast',PodcastViewSet)
router.register(r'podcastparticipant',PodcastParticipantViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
