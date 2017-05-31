from django.shortcuts import render
from django.http import HttpResponse
from .models import query

def index(request):
	html = ''
	questions = query.objects.all()
	for question in questions:
		html = '1)'+str(question)+'||'+html
	return HttpResponse(html)
