# Generated by Django 2.0.4 on 2018-04-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityjournal',
            name='end',
            field=models.DateTimeField(null=True),
        ),
    ]
