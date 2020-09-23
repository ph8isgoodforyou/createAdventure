# Generated by Django 3.1.1 on 2020-09-22 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        ('transport', '0001_initial'),
        ('pointOfInterest', '0001_initial'),
        ('accommodation', '0001_initial'),
        ('placeToEat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
                ('largest_city', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('time_zone', models.CharField(max_length=50)),
                ('fk_accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accommodation.accommodation')),
                ('fk_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.item')),
                ('fk_placeToEat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placeToEat.placetoeat')),
                ('fk_pointOfInterest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pointOfInterest.pointofinterest')),
                ('fk_transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.transport')),
            ],
        ),
    ]