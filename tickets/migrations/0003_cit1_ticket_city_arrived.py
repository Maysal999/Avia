# Generated by Django 4.2 on 2024-07-16 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_rename_city_ticket_city_flight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cit1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='city_arrived',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tickets.cit1'),
            preserve_default=False,
        ),
    ]