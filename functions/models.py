from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class ChatGPTDocument(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	document = models.FileField(upload_to=f'documents/%Y/%m/%d/%h', verbose_name='Документ')
