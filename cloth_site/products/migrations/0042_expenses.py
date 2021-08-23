# Generated by Django 3.2.6 on 2021-08-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0041_users_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenses', models.CharField(blank=True, max_length=1000, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('Date', models.CharField(blank=True, max_length=1000, null=True)),
                ('month_date', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]