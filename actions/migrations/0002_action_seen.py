# Generated by Django 4.1.7 on 2023-04-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
