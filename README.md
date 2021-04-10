# AudioApi
This repository has two folders.
1. AudioApi - Root project folder
2. AudioServer - API folder

The API uses Django Rest Framework
The Database used is SQLite3 that is prebuilt however using any other is not a problem

The following files in AudioServer folder are important:
1. models.py
2. serializers.py
3. views.py
4. urls.py

__models.py__
The API is simple and uses only text data as input however any data can be used by changing the models.py file.
The section that will allow you to upload file is commented.
The tables are:
1. Song - for storing songs data
2. Podcast - for storing podcast data
3. AudioBook - for storing audiobook data
4. PodcastParticipant - for storing the participants in a podcast

__serializer.py__
This file contains the serializers that help in converting model data to jason and visa versa.
The following are the serializers used:
1. SongSerializer - for Song Model
2. PodcastSerializer - for Podcast Model
3. AudioBookSerializer - for AudioBook Model
4. PodcastParticipantsSerializer - for PodcastParticipants Model
The serializer class aresubclasses of the Django Rest Framework's (DRF) serializer.HyperlinkedModelSerializer class

__views.py__
This file contains the views. The views used here are DRF's viewset.ModelViewSet
the following views are used:
1. SongView
2. PodcastViewSet
3. AudioBookViewSet
4. PodcastParticipantViewSet

__urls.py__
This file has rest_framework.router which is used to map url to viewsets.
