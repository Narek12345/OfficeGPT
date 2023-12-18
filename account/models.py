from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	client_id_token = models.CharField(max_length=255, blank=True, null=True)
	client_secret_token = models.CharField(max_length=255, blank=True, null=True)
	chatgpt_token = models.CharField(max_length=255, blank=True, null=True)
