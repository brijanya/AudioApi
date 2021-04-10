# Generated by Django 3.1.4 on 2021-04-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AudioServer', '0004_auto_20210409_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Song', 'song'), ('Podcast', 'podcast'), ('AudioBook', 'audiobook')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploadTime', models.DateTimeField(auto_now=True)),
                ('host', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=100, null=True)),
                ('narrator', models.CharField(max_length=100, null=True)),
                ('participants', models.ManyToManyField(to='AudioServer.PodcastParticipant')),
            ],
        ),
        migrations.DeleteModel(
            name='AudioBook',
        ),
        migrations.RemoveField(
            model_name='podcast',
            name='participants',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
        migrations.DeleteModel(
            name='Podcast',
        ),
    ]