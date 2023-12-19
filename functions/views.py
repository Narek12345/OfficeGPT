from django.views import View
from django.shortcuts import render

from .forms import AskQuestionChatGPTForm


class FunctionsView(View):
	template_name = 'functions/functions.html'

	def get(self, request):
		return render(request, self.template_name)


class AskQuestionChatGPTView(View):
	template_name = 'functions/ask_question_chatgpt.html'

	def get(self, request):
		form = AskQuestionChatGPTForm(request.GET)
		text = form.data.get('text')

		if text:
			answer = text
		else:
			answer = 'Вы не ввели текст'

		if request.user.profile.chatgpt_token:
			context = {'form': form, 'answer': answer, 'section': 'chatgpt'}
			return render(request, self.template_name, context)

		else:
			context = {'form': form, 'answer': answer, 'section': 'profile'}
			return render(request, self.template_name, context)