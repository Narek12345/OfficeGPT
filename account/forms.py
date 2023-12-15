from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Пароль',
								widget=forms.PasswordInput)
	password2 = forms.CharField(label='Повторите пароль',
								widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError("Passwords don't match.")
		return cd['password2']


class AddTokensForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['client_id_token', 'client_secret_token', 'chatgpt_token']