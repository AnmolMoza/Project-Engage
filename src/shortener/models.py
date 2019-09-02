
from django.db import models


# Create your models here.

from .utils import code_generator

class ShorURL(models.Model):
	url 		= models.CharField(max_length = 1000, )
	shortcode 	= models.CharField(max_length = 15, unique = True, blank = True)
	updated		= models.DateTimeField(auto_now = True)
	timestamp	= models.DateTimeField(auto_now_add = True)
	

	def save(self, *args, **kwargs):
		print("Something")
		if self.shortcode is None or self.shortcode == "": #If blank sets the code by itself
			self.shortcode = code_generator()
		super(ShorURL, self).save(*args, **kwargs)


	def __Str__(self):
		return str(self.url)


	def __unicode__(self):
		return str(self.url)