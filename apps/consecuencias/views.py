from django.shortcuts import render

# Create your views here.
def Home_Consecuencias(request):
	
	return render(request, 'consecuencias/home_consecuencias.html')