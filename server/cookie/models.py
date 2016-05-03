from __future__ import unicode_literals

from django.db import models


class Cookie(models.Model):
    name = models.CharField(max_length=255)
    chrome_cookie = models.FileField(upload_to='media/')
    firefox_cookie = models.FileField(upload_to='media/')

    def __unicode__(self):
        return self.name
