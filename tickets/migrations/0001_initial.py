# Generated by Django 4.2 on 2024-07-16 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeroport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aeroport', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bag', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plane', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_nomer', models.CharField(max_length=60)),
                ('flight_date', models.DateTimeField()),
                ('arrived_date', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('reassingment', models.IntegerField()),
                ('aeroport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.aeroport')),
                ('bag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.bag')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.city')),
                ('plane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.plane')),
            ],
        ),
        migrations.CreateModel(
            name='Buy_ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=70)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket')),
            ],
        ),
    ]
