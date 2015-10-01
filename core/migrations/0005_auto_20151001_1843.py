# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151001_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='users',
            new_name='user',
        ),
    ]
