# Generated by Django 3.1.1 on 2020-09-25 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finzlist', '0002_bookmark_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]