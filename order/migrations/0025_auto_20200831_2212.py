# Generated by Django 2.1.3 on 2020-08-31 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0024_auto_20200831_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 31, 22, 12, 4, 827152)),
        ),
    ]