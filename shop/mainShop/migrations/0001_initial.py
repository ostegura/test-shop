# Generated by Django 3.0.5 on 2020-05-10 13:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(default='', upload_to='category', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])])),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shoes', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])])),
                ('name', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('price', models.CharField(default='0$', max_length=64)),
                ('size', models.CharField(default='36', max_length=2)),
                ('description', models.TextField(default='')),
                ('is_active', models.BooleanField()),
                ('sale_cnt', models.PositiveIntegerField(default=0)),
                ('add_date', models.DateTimeField(auto_now=True, verbose_name='added date')),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainShop.Category')),
            ],
            options={
                'verbose_name': 'Shoes',
                'verbose_name_plural': 'Shoes',
            },
        ),
        migrations.CreateModel(
            name='ShoesGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainShop.Shoes')),
            ],
            options={
                'verbose_name': 'ShoesGallery',
                'verbose_name_plural': 'ShoesGalleries',
            },
        ),
        migrations.CreateModel(
            name='ShoesImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shoes_detail', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])])),
                ('shoes_gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainShop.ShoesGallery')),
            ],
            options={
                'verbose_name': 'ShoesImage',
                'verbose_name_plural': 'ShoesImages',
            },
        ),
    ]
