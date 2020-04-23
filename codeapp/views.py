from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html')


def register(request):
	return render(request, 'register.html')


def rankboard(request):
	return render(request, 'rankboard.html')


def dashboard(request):
	return render(request, 'dashboard.html')


def contest(request):
	return render(request, 'contest.html')


def alinks(request):
	return render(request, 'alinks.html')
