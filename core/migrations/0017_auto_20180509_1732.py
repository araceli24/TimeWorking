# Generated by Django 2.0.5 on 2018-05-09 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20180504_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityjournal',
            name='start',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 9, 17, 32, 43, 409791)),
        ),
        migrations.AlterField(
            model_name='registry',
            name='start',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 5, 9, 17, 32, 43, 412298)),
        ),
    ]