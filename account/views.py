from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import UserRegistrationForm, AddTokensForm


def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Создаем новый обьект пользователя, но пока не сохраняем его.
			new_user = user_form.save(commit=False)
			# Установить выбранный пароль.
			new_user.set_password(user_form.cleaned_data['password'])
			# Сохранить обьект User.
			new_user.save()
			# Создаем обьект Profile.
			Profile.objects.create(user=new_user)
			# Вход в систему под новым аккаунтом.
			login(request, new_user)

			return render(request, 'account/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'account/register.html', {'user_form': user_form})

    
def logout_view(request):
	logout(request)
	return redirect('dashboard:dashboard')


@login_required
def profile(request):
	return render(request, 'account/profile.html')


@require_POST
def add_tokens(request, user_id):
	"""Добавить токены в БД."""
	add_tokens_form = AddTokensForm(request.POST)
	if add_tokens_form.is_valid():
		data = add_tokens_form.data
		profile = Profile.objects.filter(user=user_id).first()
		profile.client_id_token = data['client_id_token']
		profile.client_secret_token = data['client_secret_token']
		profile.chatgpt_token = data['chatgpt_token']
		profile.save()
	else:
		# Ошибка.
		pass
	return redirect('account:profile')