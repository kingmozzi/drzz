# Generated by Django 3.2.14 on 2022-08-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mucket',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
