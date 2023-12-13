from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm


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