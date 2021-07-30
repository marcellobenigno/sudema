from django.shortcuts import render


def index(request):
	return render(request, 'core/index.html')


def pag2(request):
	return render(request, 'core/pag2.html')


def sobre(request):
	return render(request, 'core/sobre.html')
