from django.db import models

# Create your models here.
from shortener.models import ShorURL

class ClickEventManager(models.Manager):
	def create_event(self,ShorInstance):
		if isinstance(ShorInstance,ShorURL):
			obj, created = self.get_or_create(shor_url=ShorInstance)
			obj.count += 1
			obj.save()
			return obj.count
		return None

class ClickEvent(models.Model):
	shor_url 	= models.OneToOneField(ShorURL, on_delete = models.PROTECT)
	count 	 	= models.IntegerField(default=0)
	updated		= models.DateTimeField(auto_now = True)
	timestamp	= models.DateTimeField(auto_now_add = True)

	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)