# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0017_auto_20180803_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manyparent',
            name='name',
            field=models.CharField(max_length=50, db_column=b'parent_name'),
        ),
    ]
