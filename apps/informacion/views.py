from django.shortcuts import render

# Create your views here.
def Home_Informacion(request):
	
	return render(request, 'informacion/home_informacion.html')