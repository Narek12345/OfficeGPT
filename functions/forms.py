from django import forms


class AskQuestionChatGPTForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea, label='Текст')