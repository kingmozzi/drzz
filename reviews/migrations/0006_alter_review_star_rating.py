# Generated by Django 3.2 on 2022-08-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_review_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='star_rating',
            field=models.FloatField(default=0),
        ),
    ]
