# Generated by Django 2.1.2 on 2018-11-06 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0005_auto_20181106_0106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='engineer',
            options={'ordering': ['engr_team', 'engr_name']},
        ),
    ]
