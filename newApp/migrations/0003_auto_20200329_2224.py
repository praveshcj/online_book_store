# Generated by Django 3.0.4 on 2020-03-29 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0002_customer_address_is_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_of_order',
            field=models.DateTimeField(),
        ),
    ]