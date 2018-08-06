# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0011_auto_20180718_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='token',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
