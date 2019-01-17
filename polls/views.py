from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	#return HttpResponse("9/19/70 is hella heady")
	return render(request, 'polls/saint.html', {})