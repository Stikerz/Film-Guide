from django.db import models
from django.shortcuts import _get_queryset
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser

def get_object_or_none(klass, *args, **kwargs):
	queryset = _get_queryset(klass)
	try:
		return queryset.get(*args, **kwargs)
	except queryset.model.DoesNotExist:
		return None

class DateUpdate(models.Model):
	created_at = models.DateTimeField(auto_now_add=True,null=True)
	updated_at = models.DateTimeField(auto_now=True,null=True)

	class Meta:
		abstract = True

class FilmList(DateUpdate):
	title = models.CharField(max_length=1024,null=True)
	channel = models.CharField(max_length=125,null=True)
	rating = models.DecimalField(null=True,max_digits=5,decimal_places=2)
	timing = models.CharField(max_length=125,null=True)
	thumbnail = models.CharField(max_length=1024,null=True)
	profile = models.CharField(max_length=1024,null=True)
	detailed = models.CharField(max_length=1024,null=True)
	original = models.CharField(max_length=1024,null=True)

class Channels(DateUpdate):
	title = models.CharField(max_length=512)
	channel_id = models.CharField(max_length=12)	