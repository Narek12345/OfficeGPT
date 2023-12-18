from django.urls import path

from . import views

app_name = 'functions'

urlpatterns = [
	path('', views.FunctionsView.as_view(), name='functions'),
]