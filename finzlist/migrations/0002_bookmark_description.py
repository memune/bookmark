# Generated by Django 3.1.1 on 2020-09-25 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finzlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='description',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]