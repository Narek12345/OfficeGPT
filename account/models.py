from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
	client_id_token = models.CharField(max_length=255, default=None)
	client_secret_token = models.CharField(max_length=255, default=None)
	chatgpt_token = models.CharField(max_length=255, default=None)