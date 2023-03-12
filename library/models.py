from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Notes(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

	def __str__(self):
		return self.title