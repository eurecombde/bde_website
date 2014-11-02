# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='furniture_appreciation',
            field=models.PositiveSmallIntegerField(verbose_name=b'Furniture appreciation', choices=[(1, b'Poor'), (2, b'Fair'), (3, b'Good'), (4, b'Excellent'), (5, b'Unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='additionalinfo',
            name='heating_type',
            field=models.PositiveSmallIntegerField(verbose_name=b'Type of heating', choices=[(1, b'Electricity'), (2, b'Gas'), (3, b'Fuel'), (4, b'Other'), (5, b'Unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='price',
            name='agency_fees',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name=b'Angency fees', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='price',
            name='apl',
            field=models.PositiveSmallIntegerField(help_text=b"APL in euro, for 1 person (you only). Give the APL for the nominal case : student, almost no revenue, and not a scholarship holder (boursier). Leave the field empty if you don't know.", null=True, verbose_name=b'APL (Housing Benefits)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='price',
            name='council_tax',
            field=models.PositiveSmallIntegerField(help_text=b"The council tax may be included or not in the price you pay for the rent, 0 if you're not asked to pay anything, leave empty if unknown", null=True, verbose_name=b"Council tax (taxe d'habitation)", blank=True),
            preserve_default=True,
        ),
    ]
