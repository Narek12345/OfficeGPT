from django.contrib import admin

from .models import ChatGPTDocument


@admin.register(ChatGPTDocument)
class ChatGPTDocumentAdmin(admin.ModelAdmin):
	pass