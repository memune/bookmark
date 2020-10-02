# Generated by Django 3.1.1 on 2020-10-02 00:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finzlist', '0008_bookmark_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookmark',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
