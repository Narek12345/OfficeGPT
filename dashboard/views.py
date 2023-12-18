from django.shortcuts import render


def dashboard(request):
	return render(request, 'dashboard/dashboard.html')

def about(request):
	return render(request, 'dashboard/about.html')