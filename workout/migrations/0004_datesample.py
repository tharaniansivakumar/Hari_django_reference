# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0003_lap_phone_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='dateSample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(max_length=30)),
                ('cancel_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
