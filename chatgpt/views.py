from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import UploadFileForIndexingToChatGPTForm
from .index_chatgpt import index_chatgpt_file


@login_required
def upload_file_for_indexing_to_chatgpt(request):
    if request.method == 'POST':
        form = UploadFileForIndexingToChatGPTForm(request.POST, request.FILES)
        if form.is_valid():
            # Обработка загруженного файла
            uploaded_file = form.cleaned_data['file']
            # Индексируем переданный файл.
            index_chatgpt_file(uploaded_file, request.user)
    else:
        form = UploadFileForIndexingToChatGPTForm()

    return render(request, 'chatgpt/upload_file_for_indexing_to_chatgpt.html', {'form': form})