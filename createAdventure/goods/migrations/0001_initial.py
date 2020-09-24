# Generated by Django 3.1.1 on 2020-09-24 10:48

from django.db import migrations, models
import goods.api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(max_length=100)),
                ('seller', models.CharField(max_length=100)),
                ('state', models.IntegerField(choices=[(1, 'New'), (2, 'Used')], default=goods.api.models.ItemState['New'])),
                ('description', models.CharField(max_length=500)),
                ('type_of_item', models.IntegerField(choices=[(1, 'Unspecified'), (2, 'Clothing'), (3, 'Shoes'), (4, 'Glasses'), (5, 'Backpacks'), (6, 'Camping_Gear'), (7, 'Tools'), (8, 'Lights'), (9, 'Watches')], default=goods.api.models.ItemType['Unspecified'])),
            ],
        ),
    ]
