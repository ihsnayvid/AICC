# Generated by Django 2.2.4 on 2019-12-11 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='choice_four',
            new_name='qtype',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='choice_three',
        ),
    ]
