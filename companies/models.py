from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.

class Companies(models.Model):
	name = models.CharField(max_length=120, null=False, blank=False, unique=True)
	logo = models.ImageField(default='media/default.jpg', upload_to='media/')
	founder = models.CharField(max_length=230, blank=False, null=False)
	whenfounded = models.DateField(blank=False)
	description = models.TextField(blank=False, null=False)
	date_posted = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return f'{self.name}'

	def get_absolute_url(self):
		return reverse("company-detail", kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):
	    super(Companies, self).save(*args, **kwargs)

	    img = Image.open(self.logo.path)

	    if img.height > 300 or img.width > 300:
	        output_size = (300,300)
	        img.thumbnail(output_size)
	        img.save(self.logo.path)