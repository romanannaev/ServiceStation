# Generated by Django 2.2.5 on 2019-09-04 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stationApp', '0003_auto_20190904_0217'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListOrders',
            new_name='Order',
        ),
    ]
