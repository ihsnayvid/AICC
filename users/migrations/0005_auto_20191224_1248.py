# Generated by Django 2.2.4 on 2019-12-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191224_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='city',
            field=models.CharField(default='lko', max_length=200),
        ),
        migrations.AddField(
            model_name='users',
            name='clas',
            field=models.CharField(default='12', max_length=200),
        ),
        migrations.AddField(
            model_name='users',
            name='password2',
            field=models.CharField(default='1234jyoti', max_length=20),
        ),
    ]
