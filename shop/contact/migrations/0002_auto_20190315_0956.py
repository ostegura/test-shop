# Generated by Django 2.1.7 on 2019-03-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='image_height',
            field=models.IntegerField(default=40),
        ),
        migrations.AddField(
            model_name='teammember',
            name='image_width',
            field=models.IntegerField(default=40),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.ImageField(height_field='image_height', upload_to='homepage/images/teammembers', width_field='image_width'),
        ),
    ]