# Generated by Django 2.2.5 on 2019-09-12 17:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stationApp', '0005_orderapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderapplication',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
