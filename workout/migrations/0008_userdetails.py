# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0007_delete_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='userDetails',
            fields=[
                ('username', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
