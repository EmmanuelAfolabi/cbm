# Generated by Django 2.1.3 on 2020-09-02 00:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0033_auto_20200902_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 2, 1, 2, 4, 381722)),
        ),
    ]