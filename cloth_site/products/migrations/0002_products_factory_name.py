# Generated by Django 3.2.6 on 2021-08-11 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='factory_name',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
