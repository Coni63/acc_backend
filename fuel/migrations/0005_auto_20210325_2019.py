# Generated by Django 3.0.3 on 2021-03-25 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0004_auto_20210325_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='lap_time',
            new_name='lap_time_gt3',
        ),
    ]