# Generated by Django 4.1.5 on 2023-02-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
