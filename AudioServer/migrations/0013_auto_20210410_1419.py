# Generated by Django 3.1.4 on 2021-04-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AudioServer', '0012_auto_20210410_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.FileField(upload_to=''),
        ),
    ]
