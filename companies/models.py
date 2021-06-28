from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Companies(models.Model):
	name = models.CharField(max_length=120, null=False, blank=False, unique=True)
	founder = models.CharField(max_length=230, blank=False, null=False)
	whenfounded = models.DateField(blank=False)
	description = models.TextField(blank=False, null=False)
	date_posted = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return f'{self.name}'

	def get_absolute_url(self):
		return reverse("company-detail", kwargs={'pk': self.pk})