# Generated by Django 3.2 on 2022-08-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friend',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='user',
            name='mucket',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
