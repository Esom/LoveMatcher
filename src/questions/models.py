from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
	text = models.TextField()
	active = models.BooleanField(default=False)
	draft = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)


def __unicode__(self):
	return self.text[:10]
