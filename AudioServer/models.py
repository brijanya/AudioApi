from django.db import models

# Create your models here.
class Song(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
#    name = models.FileField(upload_to = 'songs/')
    duration = models.PositiveIntegerField()
    uploadTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Podcast(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
#     name = models.FileField(upload_to = 'uploads/')
    duration = models.PositiveIntegerField()
    uploadTime = models.DateTimeField(auto_now=True)
    host = models.CharField(max_length=100)
    participants = models.ManyToManyField('PodcastParticipant')

    def __str__(self):
        return str(self.name)
class AudioBook(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
#    title = models.FileField(upload_to = 'uploads/')
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploadTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PodcastParticipant(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
