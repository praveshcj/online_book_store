# Generated by Django 3.0.3 on 2020-03-21 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0010_auto_20200320_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address_no',
            field=models.IntegerField(default=0),
        ),
    ]
