# Generated by Django 3.2 on 2022-08-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0009_remove_store_star_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='star_rating',
            field=models.FloatField(default=0),
        ),
    ]
