from django.views import View
from django.shortcuts import render


class FunctionsView(View):
	template_name = 'functions/functions.html'

	def get(self, request):
		return render(request, self.template_name)