# Generated by Django 4.0 on 2021-12-24 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clanusermodel',
            name='topimage',
        ),
    ]
