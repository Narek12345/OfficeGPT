from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import os


class ChatGPTDocument(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	document = models.FileField(upload_to=f'documents/%Y/%m/%d/%h', verbose_name='Документ')


	def delete(self, *args, **kwargs):
		if self.document:
			if os.path.isfile(self.document.path):
				os.remove(self.document.path)
		super().delete(*args, **kwargs)
		