import json
import pytz
from django.db import models
from datetime import datetime
from django.conf import settings
from carson.utils import parse_created_at, write_update
from carson.managers import TrustedManager, UntrustedManager
from carson.json_field import JSONField

class Account(models.Model):
    twitter_username = models.CharField("Username", help_text="Minus the '@' sign", max_length=32)
    twitter_id = models.PositiveIntegerField("Twitter ID", editable=False, null=True)

    def __unicode__(self):
        return u"@%s" % self.twitter_username

class Tag(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

class Tweet(models.Model):
    account = models.ForeignKey(Account, null=True, related_name="tweets")
    timestamp = models.DateTimeField()
    data = JSONField()

    objects = models.Manager()
    trusted = TrustedManager()
    untrusted = UntrustedManager()

    class Meta:
        ordering = ("-timestamp", "-id")

    @classmethod
    def add(cls, tweet, twitter_ids):
        values = {
            "data": tweet,
            "timestamp": parse_created_at(tweet['created_at']),
        }

        twitter_id = tweet['user']['id']

        if twitter_id in twitter_ids:
            account = Account.objects.get(twitter_id=twitter_id)
        else:
            account = None

        values['account'] = account

        return cls.objects.create(**values)
