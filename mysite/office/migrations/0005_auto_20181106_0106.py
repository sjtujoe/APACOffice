# Generated by Django 2.1.2 on 2018-11-05 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_auto_20181106_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='dispatcher',
        ),
        migrations.AlterField(
            model_name='engineer',
            name='engr_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.Team'),
        ),
    ]
