# Generated by Django 4.2 on 2024-07-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_alter_aeroport_aeroport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy_ticket',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='aeroport',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='bag',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='city_arrived',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='city_flight',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='plane',
        ),
        migrations.AddField(
            model_name='buy_ticket',
            name='ticket',
            field=models.ManyToManyField(to='tickets.ticket'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='aeroport',
            field=models.ManyToManyField(to='tickets.aeroport'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='bag',
            field=models.ManyToManyField(to='tickets.bag'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='city_arrived',
            field=models.ManyToManyField(to='tickets.cit1'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='city_flight',
            field=models.ManyToManyField(to='tickets.city'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='plane',
            field=models.ManyToManyField(to='tickets.plane'),
        ),
    ]