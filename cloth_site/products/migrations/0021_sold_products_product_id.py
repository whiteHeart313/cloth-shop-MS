# Generated by Django 3.2.6 on 2021-08-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20210815_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold_products',
            name='product_id',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True),
        ),
    ]
