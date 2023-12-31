from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from .models import ChatGPTDocument
from .forms import AskQuestionChatGPTForm, ChatGPTDocumentForm

from .chatgpt import upload_file_for_training, make_request_in_chatgpt

import requests


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
			answer = make_request_in_chatgpt(text)
		else:
			answer = 'Вы не ввели текст'

		if request.user.profile.chatgpt_token:
			context = {'form': form, 'answer': answer, 'section': 'chatgpt'}
			return render(request, self.template_name, context)

		else:
			context = {'form': form, 'answer': answer, 'section': 'profile'}
			return render(request, self.template_name, context)


class UploadDocument(View):
	template_name = 'functions/upload_document.html'

	def post(self, request):
		form = ChatGPTDocumentForm(files=request.FILES)

		if form.is_valid():
			new_document = form.save(commit=False)
			new_document.user = request.user
			new_document.save()

			# Тренируем ChatGPT с помощью переданного файла.
			upload_file_for_training(new_document.document, request.user.profile.chatgpt_token)
			new_document.document.close()

		return render(request, self.template_name, {'form': form})


	def get(self, request):
		form = ChatGPTDocumentForm()
		return render(request, self.template_name, {'form': form})


def delete_document(request, pk):
	chatgptdocument = get_object_or_404(ChatGPTDocument, pk=pk)
	chatgptdocument.delete()

	return redirect('functions:upload_document')
