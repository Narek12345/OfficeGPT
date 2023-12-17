from django import forms

from .models import ChatGPTDocument


class UploadFileForIndexingToChatGPTForm(forms.ModelForm):
	class Meta:
		model = ChatGPTDocument
		fields = ['file']
