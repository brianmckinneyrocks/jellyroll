# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(unique=True, max_length=1000)),
                ('description', models.CharField(max_length=255)),
                ('extended', models.TextField(blank=True)),
                ('thumbnail', models.ImageField(upload_to=b'img/jellyroll/bookmarks/%Y/%m', blank=True)),
                ('thumbnail_url', models.URLField(max_length=1000, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodeCommit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('revision', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ['-revision'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodeRepository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=10, choices=[(b'svn', b'Subversion'), (b'git', b'Git')])),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('username', models.CharField(help_text=b'Your username/email for this SCM.', max_length=100)),
                ('public_changeset_template', models.URLField(help_text=b"Template for viewing a changeset publically. Use '%s' for the revision number", blank=True)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'code repositories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContentLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('identifier', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.TextField()),
                ('url', models.URLField(max_length=1000, blank=True)),
                ('timestamp', models.DateTimeField()),
                ('tags', tagging.fields.TagField(max_length=2500, blank=True)),
                ('source', models.CharField(max_length=100, blank=True)),
                ('source_id', models.TextField(blank=True)),
                ('object_str', models.TextField(blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
                ('name', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('links', models.ManyToManyField(to='jellyroll.ContentLink', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_id', models.CharField(max_length=50, unique=True, serialize=False, primary_key=True)),
                ('farm_id', models.PositiveSmallIntegerField(null=True)),
                ('server_id', models.PositiveSmallIntegerField()),
                ('secret', models.CharField(max_length=30, blank=True)),
                ('o_secret', models.CharField(max_length=30, blank=True)),
                ('taken_by', models.CharField(max_length=100, blank=True)),
                ('cc_license', models.URLField(blank=True, choices=[(b'http://creativecommons.org/licenses/by/2.0/', b'CC Attribution'), (b'http://creativecommons.org/licenses/by-nd/2.0/', b'CC Attribution-NoDerivs'), (b'http://creativecommons.org/licenses/by-nc-nd/2.0/', b'CC Attribution-NonCommercial-NoDerivs'), (b'http://creativecommons.org/licenses/by-nc/2.0/', b'CC Attribution-NonCommercial'), (b'http://creativecommons.org/licenses/by-nc-sa/2.0/', b'CC Attribution-NonCommercial-ShareAlike'), (b'http://creativecommons.org/licenses/by-sa/2.0/', b'CC Attribution-ShareAlike')])),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('comment_count', models.PositiveIntegerField(default=0, max_length=5)),
                ('local_image', models.ImageField(null=True, upload_to=b'photos/flickr/%Y/%m/%d/', blank=True)),
                ('date_uploaded', models.DateTimeField(null=True, blank=True)),
                ('date_updated', models.DateTimeField(null=True, blank=True)),
                ('_exif', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SearchEngine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('home', models.URLField()),
                ('search_template', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_name', models.CharField(max_length=250)),
                ('track_name', models.CharField(max_length=250)),
                ('url', models.URLField(max_length=1000, blank=True)),
                ('track_mbid', models.CharField(max_length=36, verbose_name=b'MusicBrainz Track ID', blank=True)),
                ('artist_mbid', models.CharField(max_length=36, verbose_name=b'MusicBrainz Artist ID', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('home', models.URLField()),
                ('embed_template', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebSearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.CharField(max_length=250)),
                ('engine', models.ForeignKey(related_name='searches', to='jellyroll.SearchEngine', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'web searches',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebSearchResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('search', models.ForeignKey(related_name='results', to='jellyroll.WebSearch',on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='video',
            name='source',
            field=models.ForeignKey(related_name='videos', to='jellyroll.VideoSource', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('content_type', 'object_id')]),
        ),
        migrations.AddField(
            model_name='codecommit',
            name='repository',
            field=models.ForeignKey(related_name='commits', to='jellyroll.CodeRepository', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
