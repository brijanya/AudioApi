# Generated by Django 3.1.4 on 2021-04-09 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AudioServer', '0007_auto_20210409_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='host',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='narrator',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
