# Generated by Django 3.1.4 on 2021-04-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AudioServer', '0015_auto_20210410_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
