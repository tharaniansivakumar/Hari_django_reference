# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0008_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='autoid',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
    ]
