from django.shortcuts import render
from django.http import HttpResponse
from .models import Attorney

def index(request):
	lawyer = Attorney.objects.all().filter(name = 'jonhs')
	context = {
		"lawyer" : lawyer
	}
	return render(request, 'index/index.html', context)
# Create your views here.
