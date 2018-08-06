# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lp_brand', models.CharField(max_length=30)),
                ('lp_name', models.CharField(max_length=30)),
                ('lp_price', models.FloatField()),
                ('lp_img', models.CharField(max_length=30)),
                ('lp_ram', models.CharField(max_length=30)),
                ('lp_rom', models.CharField(max_length=30)),
                ('lp_display', models.CharField(max_length=30)),
                ('lp_battery', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ph_brand', models.CharField(max_length=30)),
                ('ph_name', models.CharField(max_length=30)),
                ('ph_price', models.FloatField()),
                ('ph_img', models.CharField(max_length=30)),
                ('ph_ram', models.CharField(max_length=30)),
                ('ph_rom', models.CharField(max_length=30)),
                ('ph_display', models.CharField(max_length=30)),
                ('ph_battery', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prod_name', models.CharField(max_length=30)),
            ],
        ),
    ]
