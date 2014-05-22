# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'House'
        db.create_table(u'housing_house', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accomodation_name', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True, null=True, blank=True)),
            ('surface', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('accomodation_type', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('accomodation_type_other', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('number_persons', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'housing', ['House'])

        # Adding model 'AdditionalInfo'
        db.create_table(u'housing_additionalinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['housing.House'], unique=True)),
            ('floor', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('disabled_persons', self.gf('django.db.models.fields.BooleanField')()),
            ('need_car', self.gf('django.db.models.fields.BooleanField')()),
            ('parking', self.gf('django.db.models.fields.BooleanField')()),
            ('heating_type', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('climatisation', self.gf('django.db.models.fields.BooleanField')()),
            ('furniture_included', self.gf('django.db.models.fields.BooleanField')()),
            ('furniture_appreciation', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('noise_comment', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('proximity_shops', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('internet_connexion', self.gf('django.db.models.fields.BooleanField')()),
            ('internet_details', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('swimming_pool', self.gf('django.db.models.fields.BooleanField')()),
            ('garden', self.gf('django.db.models.fields.BooleanField')()),
            ('outside_equipment_comment', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
        ))
        db.send_create_signal(u'housing', ['AdditionalInfo'])

        # Adding model 'Price'
        db.create_table(u'housing_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['housing.House'], unique=True)),
            ('rent_only', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('service_charge_only', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('rent_with_service_charge', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('rent_charge_per_person', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('council_tax', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('through_agency', self.gf('django.db.models.fields.BooleanField')()),
            ('agency_fees', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('apl', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('included_gas', self.gf('django.db.models.fields.BooleanField')()),
            ('included_electricity', self.gf('django.db.models.fields.BooleanField')()),
            ('included_water', self.gf('django.db.models.fields.BooleanField')()),
            ('included_internet', self.gf('django.db.models.fields.BooleanField')()),
            ('included_telephone', self.gf('django.db.models.fields.BooleanField')()),
            ('included_cleaning', self.gf('django.db.models.fields.BooleanField')()),
            ('other_expenses', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
        ))
        db.send_create_signal(u'housing', ['Price'])

        # Adding model 'Room'
        db.create_table(u'housing_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['housing.House'])),
            ('room_type', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('other_type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('room_surface', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'housing', ['Room'])

        # Adding model 'Furniture'
        db.create_table(u'housing_furniture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['housing.House'], unique=True)),
            ('washing_machine', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('clothes_dryer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('drying_rack', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dish_washer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fridge', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('oven', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('freezer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('micro_wave', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('toaster', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dishes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('baking_tray', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('desk', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('desk_chair', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tv', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'housing', ['Furniture'])

        # Adding model 'Location'
        db.create_table(u'housing_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['housing.House'], unique=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('distance_eurecom', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'housing', ['Location'])

        # Adding model 'Travel'
        db.create_table(u'housing_travel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['housing.House'], unique=True)),
            ('time_by_car_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('time_by_car_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('time_by_bus_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('time_by_bus_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('time_by_bike_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('time_by_bike_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('time_by_foot_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('time_by_foot_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('bus_line_eurecom', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('bus_line_railroad_station', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'housing', ['Travel'])

        # Adding model 'Contact'
        db.create_table(u'housing_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['housing.House'], unique=True)),
            ('landlord_first_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('landlord_last_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('landlord_email', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('landlord_phone_number', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('landlord_comment_field', self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('agency_comment_field', self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True)),
        ))
        db.send_create_signal(u'housing', ['Contact'])

        # Adding model 'Appreciation'
        db.create_table(u'housing_appreciation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['housing.House'], unique=True)),
            ('general_description', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('strong_points', self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True)),
            ('weak_points', self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True)),
        ))
        db.send_create_signal(u'housing', ['Appreciation'])

        # Adding model 'Photo'
        db.create_table(u'housing_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['housing.House'])),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('validated', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'housing', ['Photo'])

        # Adding model 'Contributor'
        db.create_table(u'housing_contributor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'housing', ['Contributor'])

        # Adding M2M table for field houses on 'Contributor'
        m2m_table_name = db.shorten_name(u'housing_contributor_houses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contributor', models.ForeignKey(orm[u'housing.contributor'], null=False)),
            ('house', models.ForeignKey(orm[u'housing.house'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contributor_id', 'house_id'])


    def backwards(self, orm):
        # Deleting model 'House'
        db.delete_table(u'housing_house')

        # Deleting model 'AdditionalInfo'
        db.delete_table(u'housing_additionalinfo')

        # Deleting model 'Price'
        db.delete_table(u'housing_price')

        # Deleting model 'Room'
        db.delete_table(u'housing_room')

        # Deleting model 'Furniture'
        db.delete_table(u'housing_furniture')

        # Deleting model 'Location'
        db.delete_table(u'housing_location')

        # Deleting model 'Travel'
        db.delete_table(u'housing_travel')

        # Deleting model 'Contact'
        db.delete_table(u'housing_contact')

        # Deleting model 'Appreciation'
        db.delete_table(u'housing_appreciation')

        # Deleting model 'Photo'
        db.delete_table(u'housing_photo')

        # Deleting model 'Contributor'
        db.delete_table(u'housing_contributor')

        # Removing M2M table for field houses on 'Contributor'
        db.delete_table(db.shorten_name(u'housing_contributor_houses'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'housing.additionalinfo': {
            'Meta': {'object_name': 'AdditionalInfo'},
            'climatisation': ('django.db.models.fields.BooleanField', [], {}),
            'disabled_persons': ('django.db.models.fields.BooleanField', [], {}),
            'floor': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'furniture_appreciation': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'furniture_included': ('django.db.models.fields.BooleanField', [], {}),
            'garden': ('django.db.models.fields.BooleanField', [], {}),
            'heating_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'house': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['housing.House']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internet_connexion': ('django.db.models.fields.BooleanField', [], {}),
            'internet_details': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'need_car': ('django.db.models.fields.BooleanField', [], {}),
            'noise_comment': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'outside_equipment_comment': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'parking': ('django.db.models.fields.BooleanField', [], {}),
            'proximity_shops': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'swimming_pool': ('django.db.models.fields.BooleanField', [], {})
        },
        u'housing.appreciation': {
            'Meta': {'object_name': 'Appreciation'},
            'general_description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'house': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['housing.House']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'strong_points': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'weak_points': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'})
        },
        u'housing.contact': {
            'Meta': {'object_name': 'Contact'},
            'agency_comment_field': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'house': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['housing.House']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landlord_comment_field': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'landlord_email': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'landlord_first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'landlord_last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'landlord_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'housing.contributor': {
            'Meta': {'object_name': 'Contributor'},
            'houses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['housing.House']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'housing.furniture': {
            'Meta': {'object_name': 'Furniture'},
            'baking_tray': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'clothes_dryer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'desk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'desk_chair': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dish_washer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dishes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'drying_rack': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'freezer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fridge': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'house': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['housing.House']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'micro_wave': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'oven': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'toaster': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tv': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'washing_machine': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'housing.house': {
            'Meta': {'object_name': 'House'},
            'accomodation_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'accomodation_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'accomodation_type_other': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_persons': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'surface': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'housing.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'distance_eurecom': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'house': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['housing.House']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'housing.photo': {
            'Meta': {'ordering': "['pos']", 'object_name': 'Photo'},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['housing.House']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'validated': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'housing.price': {
            'Meta': {'object_name': 'Price'},
            'agency_fees': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'apl': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'council_tax': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'house': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['housing.House']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'included_cleaning': ('django.db.models.fields.BooleanField', [], {}),
            'included_electricity': ('django.db.models.fields.BooleanField', [], {}),
            'included_gas': ('django.db.models.fields.BooleanField', [], {}),
            'included_internet': ('django.db.models.fields.BooleanField', [], {}),
            'included_telephone': ('django.db.models.fields.BooleanField', [], {}),
            'included_water': ('django.db.models.fields.BooleanField', [], {}),
            'other_expenses': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'rent_charge_per_person': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'rent_only': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rent_with_service_charge': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'service_charge_only': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'through_agency': ('django.db.models.fields.BooleanField', [], {})
        },
        u'housing.room': {
            'Meta': {'ordering': "['room_type']", 'object_name': 'Room'},
            'house': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['housing.House']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'room_surface': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'room_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'housing.travel': {
            'Meta': {'object_name': 'Travel'},
            'bus_line_eurecom': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'bus_line_railroad_station': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'house': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['housing.House']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_by_bike_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_by_bike_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_by_bus_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_by_bus_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_by_car_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_by_car_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_by_foot_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_by_foot_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['housing']