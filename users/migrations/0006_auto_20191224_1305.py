# Generated by Django 2.2.4 on 2019-12-24 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191224_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='usrname',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='users',
            name='password2',
            field=models.CharField(default='1234', max_length=20),
        ),
    ]
