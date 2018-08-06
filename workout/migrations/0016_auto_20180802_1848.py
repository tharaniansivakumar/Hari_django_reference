# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0015_auto_20180802_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manychild',
            name='value',
            field=models.IntegerField(verbose_name=b'val_id'),
        ),
    ]
