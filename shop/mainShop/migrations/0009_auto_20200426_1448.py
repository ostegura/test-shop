# Generated by Django 3.0.5 on 2020-04-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainShop', '0008_shoes_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='description',
            field=models.TextField(default=''),
        ),
    ]