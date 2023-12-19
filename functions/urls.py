from django.urls import path

from . import views

app_name = 'functions'

urlpatterns = [
	path('', views.FunctionsView.as_view(), name='functions'),
	path('ask_question_chatgpt/', views.AskQuestionChatGPTView.as_view(), name='ask_question_chatgpt'),
	path('upload_document/', views.UploadDocument.as_view(), name='upload_document'),
]