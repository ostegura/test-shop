# Generated by Django 3.0.5 on 2020-05-29 08:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainShop', '0003_sizetable'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SizeTable',
        ),
        migrations.AddField(
            model_name='category',
            name='size_table',
            field=models.ImageField(default='noimage.jpg', upload_to='size_table', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg', 'webp'])]),
        ),
    ]
