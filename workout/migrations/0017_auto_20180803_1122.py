# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0016_auto_20180802_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manychild',
            name='info',
            field=models.ForeignKey(to='workout.manyparent', db_column=b'parent_name'),
        ),
        migrations.AlterField(
            model_name='manychild',
            name='value',
            field=models.IntegerField(),
        ),
    ]
