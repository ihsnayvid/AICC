# Generated by Django 2.2.4 on 2020-02-03 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0011_sresult_streamquiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sresult',
            name='Interest_1_desc',
        ),
        migrations.RemoveField(
            model_name='sresult',
            name='Interest_2_desc',
        ),
    ]
