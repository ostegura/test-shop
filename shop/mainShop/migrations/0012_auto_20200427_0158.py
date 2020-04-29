# Generated by Django 3.0.5 on 2020-04-26 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainShop', '0011_auto_20200427_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=64, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='slug',
            field=models.SlugField(max_length=128, unique=True, verbose_name='URL'),
        ),
    ]
