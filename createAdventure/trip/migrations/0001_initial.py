# Generated by Django 3.1.1 on 2020-09-22 19:32

from django.db import migrations, models
import django.db.models.deletion
import trip.api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trip_type', models.IntegerField(choices=[(1, 'The_Weekend_Break'), (2, 'The_Package_Holiday'), (3, 'The_Group_Tour'), (4, 'Road_Trip'), (5, 'Volunteer_Travel'), (6, 'The_Gap_Year'), (7, 'Event_Travel'), (8, 'Business_Travel')], default=trip.api.models.TripTypes['The_Weekend_Break'])),
                ('overall_price', models.FloatField(max_length=10000000)),
                ('list_of_items', models.CharField(max_length=1000)),
                ('fk_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.country')),
            ],
        ),
    ]
