# Generated by Django 3.1.1 on 2020-09-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='link',
            field=models.CharField(max_length=500),
        ),
    ]
