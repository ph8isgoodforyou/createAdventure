# Generated by Django 3.1.3 on 2020-11-05 12:17

import accommodation.api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('room', models.IntegerField()),
                ('accommodation_type', models.IntegerField(choices=[(1, 'Hotel'), (2, 'Hostel'), (3, 'Motel'), (4, 'Cottage'), (5, 'Mansion'), (6, 'Resort'), (7, 'Apartment'), (8, 'BandB'), (9, 'Tent'), (10, 'Yacht')], default=accommodation.api.models.AccommodationTypes['Hotel'])),
                ('price', models.FloatField(max_length=100)),
                ('rating', models.IntegerField(choices=[(1, 'ONE_STAR'), (2, 'TWO_STAR'), (3, 'THREE_STAR'), (4, 'FOUR_STAR'), (5, 'FIVE_STAR')], default=accommodation.api.models.RatingTypes['FIVE_STAR'])),
                ('date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
