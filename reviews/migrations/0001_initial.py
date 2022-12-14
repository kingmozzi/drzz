# Generated by Django 3.2 on 2022-08-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('store_id', models.IntegerField(default=0)),
                ('created_date', models.CharField(max_length=200)),
                ('contents', models.CharField(max_length=1000)),
                ('star_rating', models.IntegerField(default=0)),
            ],
        ),
    ]
