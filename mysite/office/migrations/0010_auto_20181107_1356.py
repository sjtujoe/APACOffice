# Generated by Django 2.1.2 on 2018-11-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0009_auto_20181107_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='queue',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterModelTable(
            name='advice',
            table='advice',
        ),
    ]
