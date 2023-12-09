from django.shortcuts import render

from .models import Noticia

# Create your views here.
def Home_Noticias(request):
	todas = Noticia.objects.all()
	contexto = {}
	
	contexto['noticias'] = todas
	contexto['fecha'] = '09 - 12 - 2023'

	return render(request, 'noticias/home_noticias.html', contexto)

	