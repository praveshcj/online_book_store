# Generated by Django 3.0.4 on 2020-03-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_address',
            name='is_current',
            field=models.BooleanField(default=False),
        ),
    ]