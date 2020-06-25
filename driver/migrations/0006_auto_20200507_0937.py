# Generated by Django 2.0.1 on 2020-05-07 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0005_auto_20200507_0931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambulance',
            name='ambulance_location',
        ),
        migrations.AddField(
            model_name='ambulance',
            name='chasis_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ambulance',
            name='engine_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ambulance',
            name='rc_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
