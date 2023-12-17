from django.urls import path

from . import views

app_name = 'chatgpt'

urlpatterns = [
	path('upload_file_for_indexing_to_chatgpt/', views.upload_file_for_indexing_to_chatgpt, name='upload_file_for_indexing_to_chatgpt'),
]