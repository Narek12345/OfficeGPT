# Generated by Django 5.0 on 2023-12-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgptdocument',
            name='document',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
