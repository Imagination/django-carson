# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Account.active'
        db.add_column('carson_account', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Tag.active'
        db.add_column('carson_tag', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Account.active'
        db.delete_column('carson_account', 'active')

        # Deleting field 'Tag.active'
        db.delete_column('carson_tag', 'active')


    models = {
        'carson.account': {
            'Meta': {'object_name': 'Account'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'twitter_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'carson.tag': {
            'Meta': {'object_name': 'Tag'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'carson.tweet': {
            'Meta': {'ordering': "('-timestamp', '-status_id')", 'object_name': 'Tweet'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tweets'", 'null': 'True', 'to': "orm['carson.Account']"}),
            'data': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['carson']