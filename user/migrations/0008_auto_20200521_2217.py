# Generated by Django 2.0.1 on 2020-05-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_usercoordinates_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoordinates',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
