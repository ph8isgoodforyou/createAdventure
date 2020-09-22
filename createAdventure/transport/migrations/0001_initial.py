# Generated by Django 3.1.1 on 2020-09-22 19:32

from django.db import migrations, models
import transport.api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transportation_type', models.IntegerField(choices=[(1, 'Plane'), (2, 'Ship'), (3, 'Bus'), (4, 'Train'), (5, 'Car'), (6, 'ByFoot'), (7, 'Bicycle')], default=transport.api.models.TransportationTypes['Plane'])),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=100)),
                ('date_available', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
