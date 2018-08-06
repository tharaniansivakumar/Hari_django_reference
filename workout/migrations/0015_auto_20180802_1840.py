# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0014_auto_20180802_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manychild',
            name='info',
            field=models.ForeignKey(verbose_name=b'parent_name', to='workout.manyparent'),
        ),
    ]
