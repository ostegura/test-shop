# Generated by Django 2.1.7 on 2019-03-18 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20190315_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='number',
            field=models.CharField(max_length=25),
        ),
    ]
