from django.db import models


class Profile(models.Model):
	client_id_token = models.CharField(max_length=255)
	client_secret_token = models.CharField(max_length=255)
	chatgpt_token = models.CharField(max_length=255)