from django.shortcuts import render

# Create your views here.
def Home_Causas(request):
	
	return render(request, 'causas/home_causas.html')