# Generated by Django 2.2.4 on 2019-12-23 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clg_name', models.CharField(max_length=200)),
                ('clg_loc', models.CharField(max_length=200)),
                ('clg_top_field', models.TextField()),
                ('clg_city', models.CharField(max_length=200)),
                ('clg_website', models.CharField(max_length=300)),
                ('clg_phno', models.CharField(max_length=10)),
                ('clg_country', models.CharField(max_length=200)),
            ],
        ),
    ]
