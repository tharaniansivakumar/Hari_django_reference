# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0006_auto_20180716_0552'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userDetails',
        ),
    ]
