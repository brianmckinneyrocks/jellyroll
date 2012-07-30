# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table('jellyroll_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=1000, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('tags', self.gf('tagging.fields.TagField')(default='', max_length=2500)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('source_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('object_str', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('jellyroll', ['Item'])

        # Adding unique constraint on 'Item', fields ['content_type', 'object_id']
        db.create_unique('jellyroll_item', ['content_type_id', 'object_id'])

        # Adding model 'Photo'
        db.create_table('jellyroll_photo', (
            ('photo_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, primary_key=True)),
            ('server_id', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('taken_by', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cc_license', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('comment_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, max_length=5)),
            ('date_uploaded', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('_exif', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('jellyroll', ['Photo'])

        # Adding model 'Status'
        db.create_table('jellyroll_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('jellyroll', ['Status'])

        # Adding model 'Location'
        db.create_table('jellyroll_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.TextField')()),
            ('latitude', self.gf('django.db.models.fields.TextField')()),
            ('display_location', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('place_id', self.gf('django.db.models.fields.TextField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')()),
            ('scope', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('jellyroll', ['Location'])


    def backwards(self, orm):
        # Removing unique constraint on 'Item', fields ['content_type', 'object_id']
        db.delete_unique('jellyroll_item', ['content_type_id', 'object_id'])

        # Deleting model 'Item'
        db.delete_table('jellyroll_item')

        # Deleting model 'Photo'
        db.delete_table('jellyroll_photo')

        # Deleting model 'Status'
        db.delete_table('jellyroll_status')

        # Deleting model 'Location'
        db.delete_table('jellyroll_location')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jellyroll.item': {
            'Meta': {'ordering': "['-timestamp']", 'unique_together': "[('content_type', 'object_id')]", 'object_name': 'Item'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {}),
            'object_str': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'source_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'default': "''", 'max_length': '2500'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'blank': 'True'})
        },
        'jellyroll.location': {
            'Meta': {'ordering': "['-created_on']", 'object_name': 'Location'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {}),
            'display_location': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.TextField', [], {}),
            'longitude': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'place_id': ('django.db.models.fields.TextField', [], {}),
            'scope': ('django.db.models.fields.TextField', [], {})
        },
        'jellyroll.photo': {
            'Meta': {'object_name': 'Photo'},
            '_exif': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cc_license': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'comment_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '5'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_uploaded': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photo_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'server_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'taken_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'jellyroll.status': {
            'Meta': {'ordering': "['-date_published']", 'object_name': 'Status'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['jellyroll']