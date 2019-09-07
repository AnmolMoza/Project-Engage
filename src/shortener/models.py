
from django.db import models

# Create your models here.

from .utils import code_generator, create_shortcode
from .validators import validate_url
from django.conf import settings
from django_hosts.resolvers import reverse

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15) #when got to use in other project too
#SHOTCODE_MAX = settings.SHORTCODE_MAX   #when we dont have reusable ap


class ShorURLManager(models.Manager): #Filer out active shortcodes, Model manager
	def all(self, *args, **kwargs):
		qs_main = super(ShorURLManager,self).all(*args, **kwargs)
		qs 		= qs_main.filter(active = True)
		return qs

	def	refresh_shortcode(self, items = None): #Refreshing Shortcodes and giving number of new short codes
		qs = ShorURL.objects.filter(id__gte = 1)
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.shortcode)
			q.save()
			new_codes += 1
		return "new_code made: {i}".format(i=new_codes)


class ShorURL(models.Model):
	url 		= models.CharField(max_length = 1000, validators = [validate_url])
	shortcode 	= models.CharField(max_length = SHORTCODE_MAX, unique = True, blank = True)
	updated		= models.DateTimeField(auto_now = True)
	timestamp	= models.DateTimeField(auto_now_add = True)
	active		= models.BooleanField(default = True)
	objects		= ShorURLManager()
	
	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "": #If blank sets the code by itself
			self.shortcode = create_shortcode(self)
		if not "http" in self.url:
			self.url = "http://" + self.url
		super(ShorURL, self).save(*args, **kwargs)


	def __Str__(self):
		return str(self.url)


	def __unicode__(self):
		return str(self.url)


	def get_short_url(self):
		url_path = reverse("scode", kwargs={'shortcode':self.shortcode}, host='www', scheme='http')
		return url_path