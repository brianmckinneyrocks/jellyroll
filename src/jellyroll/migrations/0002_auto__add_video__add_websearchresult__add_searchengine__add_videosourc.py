# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table('jellyroll_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videos', to=orm['jellyroll.VideoSource'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('jellyroll', ['Video'])

        # Adding model 'WebSearchResult'
        db.create_table('jellyroll_websearchresult', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('search', self.gf('django.db.models.fields.related.ForeignKey')(related_name='results', to=orm['jellyroll.WebSearch'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('jellyroll', ['WebSearchResult'])

        # Adding model 'SearchEngine'
        db.create_table('jellyroll_searchengine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('home', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('search_template', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('jellyroll', ['SearchEngine'])

        # Adding model 'VideoSource'
        db.create_table('jellyroll_videosource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('home', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('embed_template', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('jellyroll', ['VideoSource'])

        # Adding model 'CodeRepository'
        db.create_table('jellyroll_coderepository', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('public_changeset_template', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('jellyroll', ['CodeRepository'])

        # Adding model 'Message'
        db.create_table('jellyroll_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('jellyroll', ['Message'])

        # Adding M2M table for field links on 'Message'
        db.create_table('jellyroll_message_links', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('message', models.ForeignKey(orm['jellyroll.message'], null=False)),
            ('contentlink', models.ForeignKey(orm['jellyroll.contentlink'], null=False))
        ))
        db.create_unique('jellyroll_message_links', ['message_id', 'contentlink_id'])

        # Adding model 'CodeCommit'
        db.create_table('jellyroll_codecommit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('repository', self.gf('django.db.models.fields.related.ForeignKey')(related_name='commits', to=orm['jellyroll.CodeRepository'])),
            ('revision', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('jellyroll', ['CodeCommit'])

        # Adding model 'WebSearch'
        db.create_table('jellyroll_websearch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('engine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='searches', to=orm['jellyroll.SearchEngine'])),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('jellyroll', ['WebSearch'])

        # Adding model 'Bookmark'
        db.create_table('jellyroll_bookmark', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=1000)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('extended', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=1000, blank=True)),
        ))
        db.send_create_signal('jellyroll', ['Bookmark'])

        # Adding model 'Track'
        db.create_table('jellyroll_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('track_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=1000, blank=True)),
            ('track_mbid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('artist_mbid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
        ))
        db.send_create_signal('jellyroll', ['Track'])

        # Adding model 'ContentLink'
        db.create_table('jellyroll_contentlink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('jellyroll', ['ContentLink'])

        # Deleting field 'Location.created_on'
        db.delete_column('jellyroll_location', 'created_on')

        # Deleting field 'Location.scope'
        db.delete_column('jellyroll_location', 'scope')

        # Deleting field 'Location.place_id'
        db.delete_column('jellyroll_location', 'place_id')

        # Deleting field 'Location.display_location'
        db.delete_column('jellyroll_location', 'display_location')


        # Changing field 'Location.name'
        db.alter_column('jellyroll_location', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))
        # Adding field 'Photo.farm_id'
        db.add_column('jellyroll_photo', 'farm_id',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table('jellyroll_video')

        # Deleting model 'WebSearchResult'
        db.delete_table('jellyroll_websearchresult')

        # Deleting model 'SearchEngine'
        db.delete_table('jellyroll_searchengine')

        # Deleting model 'VideoSource'
        db.delete_table('jellyroll_videosource')

        # Deleting model 'CodeRepository'
        db.delete_table('jellyroll_coderepository')

        # Deleting model 'Message'
        db.delete_table('jellyroll_message')

        # Removing M2M table for field links on 'Message'
        db.delete_table('jellyroll_message_links')

        # Deleting model 'CodeCommit'
        db.delete_table('jellyroll_codecommit')

        # Deleting model 'WebSearch'
        db.delete_table('jellyroll_websearch')

        # Deleting model 'Bookmark'
        db.delete_table('jellyroll_bookmark')

        # Deleting model 'Track'
        db.delete_table('jellyroll_track')

        # Deleting model 'ContentLink'
        db.delete_table('jellyroll_contentlink')


        # User chose to not deal with backwards NULL issues for 'Location.created_on'
        raise RuntimeError("Cannot reverse this migration. 'Location.created_on' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Location.scope'
        raise RuntimeError("Cannot reverse this migration. 'Location.scope' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Location.place_id'
        raise RuntimeError("Cannot reverse this migration. 'Location.place_id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Location.display_location'
        raise RuntimeError("Cannot reverse this migration. 'Location.display_location' and its values cannot be restored.")

        # Changing field 'Location.name'
        db.alter_column('jellyroll_location', 'name', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'Photo.farm_id'
        db.delete_column('jellyroll_photo', 'farm_id')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jellyroll.bookmark': {
            'Meta': {'object_name': 'Bookmark'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'extended': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '1000'})
        },
        'jellyroll.codecommit': {
            'Meta': {'ordering': "['-revision']", 'object_name': 'CodeCommit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'commits'", 'to': "orm['jellyroll.CodeRepository']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'jellyroll.coderepository': {
            'Meta': {'object_name': 'CodeRepository'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'public_changeset_template': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jellyroll.contentlink': {
            'Meta': {'object_name': 'ContentLink'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.TextField', [], {}),
            'longitude': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'jellyroll.message': {
            'Meta': {'object_name': 'Message'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['jellyroll.ContentLink']", 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {})
        },
        'jellyroll.photo': {
            'Meta': {'object_name': 'Photo'},
            '_exif': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cc_license': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'comment_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '5'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_uploaded': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'farm_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'photo_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'server_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'taken_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'jellyroll.searchengine': {
            'Meta': {'object_name': 'SearchEngine'},
            'home': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'search_template': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'jellyroll.status': {
            'Meta': {'ordering': "['-date_published']", 'object_name': 'Status'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jellyroll.track': {
            'Meta': {'object_name': 'Track'},
            'artist_mbid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'artist_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'track_mbid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'track_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'blank': 'True'})
        },
        'jellyroll.video': {
            'Meta': {'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['jellyroll.VideoSource']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'jellyroll.videosource': {
            'Meta': {'object_name': 'VideoSource'},
            'embed_template': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'home': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'jellyroll.websearch': {
            'Meta': {'object_name': 'WebSearch'},
            'engine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'searches'", 'to': "orm['jellyroll.SearchEngine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'jellyroll.websearchresult': {
            'Meta': {'object_name': 'WebSearchResult'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'search': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'results'", 'to': "orm['jellyroll.WebSearch']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['jellyroll']