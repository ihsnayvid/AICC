# Generated by Django 2.2.4 on 2020-02-08 05:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0012_auto_20200203_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='Interest_1_desc',
        ),
        migrations.RemoveField(
            model_name='result',
            name='Interest_2_desc',
        ),
        migrations.AddField(
            model_name='result',
            name='Date_Created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='sresult',
            name='Date_Created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
