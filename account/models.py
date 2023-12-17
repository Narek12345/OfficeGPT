from django.db import models
from django.conf import settings


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	client_id_token = models.CharField(max_length=255, blank=True, null=True)
	client_secret_token = models.CharField(max_length=255, blank=True, null=True)
	chatgpt_token = models.CharField(max_length=255, blank=True, null=True)
