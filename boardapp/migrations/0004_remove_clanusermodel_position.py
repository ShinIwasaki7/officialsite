# Generated by Django 4.0 on 2021-12-24 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_clanusermodel_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clanusermodel',
            name='position',
        ),
    ]
