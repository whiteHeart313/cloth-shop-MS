# Generated by Django 3.2.6 on 2021-08-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0048_bills_numofitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='numOfItems',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=19, null=True),
        ),
    ]
