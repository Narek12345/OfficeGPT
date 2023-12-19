from django import forms

from .models import ChatGPTDocument


class AskQuestionChatGPTForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea, label='Текст')


class ChatGPTDocumentForm(forms.ModelForm):
	class Meta:
		model = ChatGPTDocument
		fields = ['document']
