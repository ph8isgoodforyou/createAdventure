# Generated by Django 3.1.1 on 2020-09-24 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='fk_item',
        ),
    ]
