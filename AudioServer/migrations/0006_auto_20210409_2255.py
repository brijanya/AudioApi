# Generated by Django 3.1.4 on 2021-04-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AudioServer', '0005_auto_20210409_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(choices=[('song', 'Song'), ('podcast', 'Podcast'), ('audiobook', 'AudioBook')], max_length=100),
        ),
    ]
