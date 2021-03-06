# Generated by Django 3.1.4 on 2021-04-10 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AudioServer', '0011_auto_20210410_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='title',
            field=models.FileField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='name',
            field=models.FileField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
