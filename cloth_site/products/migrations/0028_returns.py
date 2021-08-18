# Generated by Django 3.2.6 on 2021-08-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20210817_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='returns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('discounts', models.DecimalField(blank=True, decimal_places=3, max_digits=19, null=True)),
                ('Date', models.CharField(default='', max_length=10)),
                ('product_name', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
