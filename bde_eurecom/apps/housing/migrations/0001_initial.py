# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('floor', models.PositiveSmallIntegerField(help_text=b'Floor of the entrance door, considering that the street is on floor 0', verbose_name=b'Floor')),
                ('disabled_persons', models.BooleanField(verbose_name=b'Access for disabled persons')),
                ('need_car', models.BooleanField(verbose_name=b'Strongly advised that at least one person has a car')),
                ('parking', models.BooleanField(verbose_name=b'Parking')),
                ('furniture_included', models.BooleanField(verbose_name=b'Furniture included in the accomodation')),
                ('furniture_appreciation', models.PositiveSmallIntegerField(verbose_name=b'Furniture appreciation', choices=[(1, b'Poor'), (2, b'Fair'), (3, b'Good'), (4, b'Excellent')])),
                ('heating_type', models.PositiveSmallIntegerField(verbose_name=b'Type of heating', choices=[(1, b'Electricity'), (2, b'Gas'), (3, b'Fuel'), (4, b'Other')])),
                ('climatisation', models.BooleanField(verbose_name=b'Climatisation')),
                ('internet_connexion', models.BooleanField(verbose_name=b'Internet connexion provided in the accomodation')),
                ('internet_details', models.CharField(help_text=b'Comment on the internet service provided (box, phone, TV...)', max_length=300, null=True, verbose_name=b'Internet details', blank=True)),
                ('swimming_pool', models.BooleanField(verbose_name=b'Swimming pool')),
                ('garden', models.BooleanField(verbose_name=b'Garden')),
                ('outside_equipment_comment', models.CharField(help_text=b'Precise any other out-door equipment or infrastructure (e.g.: ping-pong, tennis...), or add here your comments on the garden and the swimming pool', max_length=400, null=True, verbose_name=b'Outside equipment', blank=True)),
                ('noise_comment', models.CharField(help_text=b'Comment the noise atmosphere arround the accomodation (quiet, unexpected noise...)', max_length=300, null=True, verbose_name=b'Noise comment', blank=True)),
                ('proximity_shops', models.CharField(help_text=b'Comment about the shops arround the (advantages of near shops, or drawbacks)', max_length=300, null=True, verbose_name=b'Proximity shops', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Appreciation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('general_description', models.CharField(max_length=1000, null=True, verbose_name=b'Give a general description of the accomodation, anything you want to talk about', blank=True)),
                ('strong_points', models.CharField(max_length=600, null=True, verbose_name=b'Strong points of the accomodation', blank=True)),
                ('weak_points', models.CharField(max_length=600, null=True, verbose_name=b'Weak points of the accomodation', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('landlord_first_name', models.CharField(max_length=30, null=True, verbose_name=b"Landlord's first name", blank=True)),
                ('landlord_last_name', models.CharField(max_length=30, null=True, verbose_name=b"Landlord's last name", blank=True)),
                ('landlord_email', models.CharField(max_length=70, null=True, verbose_name=b"Landlord's email", blank=True)),
                ('landlord_phone_number', models.CharField(max_length=25, null=True, verbose_name=b"Landlord's phone number", blank=True)),
                ('landlord_comment_field', models.CharField(max_length=600, null=True, verbose_name=b'Comment about the landlord', blank=True)),
                ('agency_name', models.CharField(max_length=50, null=True, verbose_name=b'Agency name', blank=True)),
                ('agency_comment_field', models.CharField(max_length=600, null=True, verbose_name=b'Comment about the agency', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('promo', models.PositiveSmallIntegerField(null=True, verbose_name=b'Promo', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('washing_machine', models.BooleanField(default=False, verbose_name=b'Washing machine')),
                ('clothes_dryer', models.BooleanField(default=False, verbose_name=b'Clothes dryer')),
                ('drying_rack', models.BooleanField(default=False, verbose_name=b'Drying rack (etendoir)')),
                ('dish_washer', models.BooleanField(default=False, verbose_name=b'Dish washer')),
                ('fridge', models.BooleanField(default=False, verbose_name=b'Fridge')),
                ('oven', models.BooleanField(default=False, verbose_name=b'Oven')),
                ('freezer', models.BooleanField(default=False, verbose_name=b'Freezer')),
                ('micro_wave', models.BooleanField(default=False, verbose_name=b'Micro-wave')),
                ('toaster', models.BooleanField(default=False, verbose_name=b'Toaster')),
                ('dishes', models.BooleanField(default=False, verbose_name=b'Dishes')),
                ('baking_tray', models.BooleanField(default=False, verbose_name=b'Baking tray (plaque de cuisson)')),
                ('desk', models.BooleanField(default=False, verbose_name=b'Desk(s)')),
                ('desk_chair', models.BooleanField(default=False, verbose_name=b'Desk chair(s)')),
                ('tv', models.BooleanField(default=False, verbose_name=b'TV')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accomodation_name', models.CharField(help_text=b'If you don\'t know what to put, you can write something including the accomodation type and the name of the landlord, like "Apartment Smith"', unique=True, max_length=30, verbose_name=b'Accomodation Name')),
                ('surface', models.PositiveSmallIntegerField(help_text=b'in m2', verbose_name=b'Surface Area')),
                ('accomodation_type', models.PositiveSmallIntegerField(verbose_name=b'Accomodation type', choices=[(1, b'House'), (2, b'Apartment'), (3, b'Studio'), (4, b"Home stay (vie chez l'habitant)"), (5, b'Student residence'), (0, b'Other')])),
                ('accomodation_type_other', models.CharField(help_text=b'Precise your accomodation type here if you have chosen other', max_length=30, null=True, verbose_name=b'Other', blank=True)),
                ('number_persons', models.PositiveSmallIntegerField(help_text=b'Number of persons the house can accomodate', verbose_name=b'Number of persons')),
                ('available', models.BooleanField(default=True, verbose_name=b'Accomodation available')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=50, verbose_name=b'Address')),
                ('city', models.CharField(max_length=50, verbose_name=b'City')),
                ('postal_code', models.CharField(max_length=5, verbose_name=b'Postal code')),
                ('distance_eurecom', models.FloatField(help_text=b'Auto-generate it by clicking your position on the map', verbose_name=b'Distance to Eurecom (in km)')),
                ('latitude', models.FloatField(help_text=b'Auto-generate it by clicking your position on the map', verbose_name=b'Latitude')),
                ('longitude', models.FloatField(help_text=b'Auto-generate it by clicking your position on the map', verbose_name=b'Longitude')),
                ('house', models.OneToOneField(to='housing.House')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'housing')),
                ('thumbnail', models.ImageField(null=True, upload_to=b'housing/thumbnails', blank=True)),
                ('descr', models.CharField(max_length=30, null=True, verbose_name=b'Description', blank=True)),
                ('pos', models.PositiveSmallIntegerField(null=True, verbose_name=b'Position', blank=True)),
                ('validated', models.BooleanField(default=False)),
                ('house', models.ForeignKey(to='housing.House')),
            ],
            options={
                'ordering': ['pos'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rent_only', models.PositiveSmallIntegerField(help_text=b'Total rent (not divided by the number of persons), in euros', null=True, verbose_name=b'Rent only', blank=True)),
                ('service_charge_only', models.PositiveSmallIntegerField(help_text=b'Total, in euros', null=True, verbose_name=b'Service charge only (charges)', blank=True)),
                ('rent_with_service_charge', models.PositiveSmallIntegerField(help_text=b'In euros. This field is only in case you don\'t have the detail of the rent and the service charge, leave it if you filled "Rent only" and "Service charge only" fields', verbose_name=b'Rent with service charge')),
                ('rent_charge_per_person', models.PositiveSmallIntegerField(verbose_name=b'Rent with service charge per person', editable=False)),
                ('council_tax', models.PositiveSmallIntegerField(verbose_name=b"Council tax (taxe d'habitation)")),
                ('through_agency', models.BooleanField(verbose_name=b'Rent through an agency')),
                ('agency_fees', models.PositiveSmallIntegerField(default=0, verbose_name=b'Angency fees')),
                ('apl', models.PositiveSmallIntegerField(help_text=b'APL in euro, for 1 person (you only)', null=True, verbose_name=b'APL (Housing Benefits)', blank=True)),
                ('included_gas', models.BooleanField(verbose_name=b'Gas')),
                ('included_electricity', models.BooleanField(verbose_name=b'Electricity')),
                ('included_water', models.BooleanField(verbose_name=b'Water')),
                ('included_internet', models.BooleanField(verbose_name=b'Internet')),
                ('included_telephone', models.BooleanField(verbose_name=b'Telephone')),
                ('included_cleaning', models.BooleanField(verbose_name=b'Cleaning services')),
                ('other_expenses', models.CharField(help_text=b'Precise the price of the service charges that are not included and that you have to pay.', max_length=400, null=True, verbose_name=b'Other expenses', blank=True)),
                ('house', models.OneToOneField(to='housing.House')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_type', models.PositiveSmallIntegerField(verbose_name=b'Room type', choices=[(1, b'Bedroom'), (2, b'Living room'), (3, b'Kitchen'), (4, b'Studio all-in-one (main room with kitchen)'), (5, b'Bathroom without toilets'), (6, b'Bathroom with toilets'), (7, b'Toilets alone'), (8, b'Garage'), (9, b'Storeroom'), (10, b'Other')])),
                ('other_type', models.CharField(help_text=b'Precise if you selected "other" as room type', max_length=30, null=True, verbose_name=b'Other', blank=True)),
                ('room_surface', models.PositiveSmallIntegerField(null=True, verbose_name=b'Estimation of surface area (if relevent)', blank=True)),
                ('house', models.ForeignKey(to='housing.House')),
            ],
            options={
                'ordering': ['room_type'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_by_car_max', models.PositiveSmallIntegerField(null=True, verbose_name=b'Max time by car', blank=True)),
                ('time_by_car_min', models.PositiveSmallIntegerField(null=True, verbose_name=b'Min time by car', blank=True)),
                ('time_by_bus_max', models.PositiveSmallIntegerField(null=True, verbose_name=b'Max time by bus', blank=True)),
                ('time_by_bus_min', models.PositiveSmallIntegerField(null=True, verbose_name=b'Min time by bus', blank=True)),
                ('time_by_bike_max', models.PositiveSmallIntegerField(null=True, verbose_name=b'Max time by bike', blank=True)),
                ('time_by_bike_min', models.PositiveSmallIntegerField(null=True, verbose_name=b'Min time by bike', blank=True)),
                ('time_by_foot_max', models.PositiveSmallIntegerField(null=True, verbose_name=b'Max time by foot', blank=True)),
                ('time_by_foot_min', models.PositiveSmallIntegerField(null=True, verbose_name=b'Min time by foot', blank=True)),
                ('bus_line_eurecom', models.CharField(max_length=300, null=True, verbose_name=b"Which bus line to go to Eurecom, and any comment about it. Precise if it's not possible to go by bus", blank=True)),
                ('bus_line_railroad_station', models.CharField(max_length=300, null=True, verbose_name=b"Which bus line to go to the nearest railroad station, and any comment about it. Precise if it's not possible to go by bus", blank=True)),
                ('house', models.OneToOneField(to='housing.House')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='furniture',
            name='house',
            field=models.OneToOneField(to='housing.House'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contributor',
            name='houses',
            field=models.ManyToManyField(to='housing.House', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='house',
            field=models.OneToOneField(to='housing.House'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appreciation',
            name='house',
            field=models.OneToOneField(to='housing.House'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='additionalinfo',
            name='house',
            field=models.OneToOneField(to='housing.House'),
            preserve_default=True,
        ),
    ]
