# Generated by Django 3.0.3 on 2020-03-24 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0019_auto_20200324_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cancellation_remarks',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='cancelled_by',
            field=models.CharField(max_length=20, null=True),
        ),
    ]