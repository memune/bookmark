# Generated by Django 3.1.1 on 2020-09-25 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finzlist', '0006_auto_20200925_0528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='category_name',
            new_name='category',
        ),
    ]
