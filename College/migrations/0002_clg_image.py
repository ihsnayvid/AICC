# Generated by Django 2.2.4 on 2019-12-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clg',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='clg_pics'),
        ),
    ]
