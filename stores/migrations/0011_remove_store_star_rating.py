# Generated by Django 3.2 on 2022-08-22 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0010_store_star_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='star_rating',
        ),
    ]
