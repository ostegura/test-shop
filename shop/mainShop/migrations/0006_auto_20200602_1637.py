# Generated by Django 3.0.5 on 2020-06-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainShop', '0005_auto_20200601_1335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренды'},
        ),
        migrations.AddField(
            model_name='shoes',
            name='articul',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='shoes',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]