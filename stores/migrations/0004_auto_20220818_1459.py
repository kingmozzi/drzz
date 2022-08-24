# Generated by Django 3.2 on 2022-08-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20220815_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='store',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='store',
            name='schedule',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='store',
            name='signature',
            field=models.CharField(default='', max_length=200),
        ),
    ]
