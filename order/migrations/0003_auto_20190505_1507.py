# Generated by Django 2.2 on 2019-05-05 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190503_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='booking',
            new_name='booking_detail',
        ),
    ]
