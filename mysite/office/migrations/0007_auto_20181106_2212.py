# Generated by Django 2.1.2 on 2018-11-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0006_auto_20181106_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer',
            name='vote',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
