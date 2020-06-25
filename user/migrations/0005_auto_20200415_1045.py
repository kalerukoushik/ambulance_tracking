# Generated by Django 2.0.1 on 2020-04-15 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_usercoordinates_driver_picked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercoordinates',
            name='driver_picked',
        ),
        migrations.AddField(
            model_name='usercoordinates',
            name='driver_loc',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]