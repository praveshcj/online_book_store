# Generated by Django 3.0.3 on 2020-03-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0009_auto_20200320_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.AddField(
            model_name='book_available',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book_ordered',
            name='no_of_copies',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer_address',
            name='address_no',
            field=models.IntegerField(),
        ),
    ]