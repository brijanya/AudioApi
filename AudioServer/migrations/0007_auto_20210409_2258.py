# Generated by Django 3.1.4 on 2021-04-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AudioServer', '0006_auto_20210409_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='author',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AlterField(
            model_name='type',
            name='host',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AlterField(
            model_name='type',
            name='narrator',
            field=models.CharField(default='Null', max_length=100),
        ),
    ]
