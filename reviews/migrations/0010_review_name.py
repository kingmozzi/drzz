# Generated by Django 3.2 on 2022-08-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_remove_review_star_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]