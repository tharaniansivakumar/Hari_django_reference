# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0012_userdetails_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='csvData',
            fields=[
                ('rollno', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
    ]
