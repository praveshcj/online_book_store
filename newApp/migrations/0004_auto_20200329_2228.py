# Generated by Django 3.0.4 on 2020-03-29 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0003_auto_20200329_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_of_order',
            field=models.DateTimeField(null=True),
        ),
    ]
