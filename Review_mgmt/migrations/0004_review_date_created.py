# Generated by Django 2.2.4 on 2020-02-11 10:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Review_mgmt', '0003_remove_review_sentiments'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Date_Created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
