from django.shortcuts import render

# Create your views here.
def Home_Solucion(request):
	
	return render(request, 'solucion/home_solucion.html')