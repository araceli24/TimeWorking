# Generated by Django 2.0.4 on 2018-04-30 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180430_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityjournal',
            name='start',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 4, 30, 13, 39, 13, 137387)),
        ),
        migrations.AlterField(
            model_name='registry',
            name='start',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 4, 30, 13, 39, 13, 139901)),
        ),
    ]