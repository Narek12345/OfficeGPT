from django.db import models
from django.conf import settings


class ChatGPTDocument(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	file = models.FileField(upload_to='uploads/')
