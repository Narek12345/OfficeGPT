from django.db import models
from django.conf import settings


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	client_id_token = models.CharField(max_length=255, null=True, default=None)
	client_secret_token = models.CharField(max_length=255, null=True, default=None)
	chatgpt_token = models.CharField(max_length=255, null=True, default=None)
