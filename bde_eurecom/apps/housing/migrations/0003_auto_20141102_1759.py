# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_auto_20141102_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='agency_fees',
            field=models.PositiveSmallIntegerField(help_text=b"Leave empty if you know there are agency fees, but you don't know how much", null=True, verbose_name=b'Angency fees', blank=True),
            preserve_default=True,
        ),
    ]
