# Generated by Django 2.2 on 2019-05-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0024_auto_20190505_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='privilege',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'Wifi'), (1, 'Breakfast')], null=True),
        ),
    ]
