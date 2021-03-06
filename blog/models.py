from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.user')
	title  = models.CharField(max_length=250)
	text = models.TextField(max_length=2000)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	image_url = models.CharField(max_length=2000)


	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title

