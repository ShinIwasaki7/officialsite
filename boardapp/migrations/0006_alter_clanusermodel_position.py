# Generated by Django 4.0 on 2021-12-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0005_clanusermodel_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clanusermodel',
            name='position',
            field=models.CharField(choices=[('リーダー', '0'), ('サブリーダー', '1'), ('長老', '2'), ('メンバー', '3')], max_length=50),
        ),
    ]
