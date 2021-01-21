from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	date_completed = models.DateTimeField(default=timezone.now)
	language = models.CharField(max_length=100)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('project_detail', kwargs={'pk': self.pk})
