# Generated by Django 2.2 on 2019-04-25 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_auto_20190425_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetail',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='booking.Room'),
        ),
    ]