# Generated by Django 2.1.2 on 2018-11-05 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_auto_20181106_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer',
            name='engr_team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='office.Team'),
        ),
    ]
