# Generated by Django 2.1.3 on 2020-09-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20200906_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('bonnet', 'bonnet'), ('gown', 'gown'), ('short', 'short')], default='gown', max_length=30),
            preserve_default=False,
        ),
    ]