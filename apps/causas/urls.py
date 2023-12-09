from django.urls import path
from . import views

app_name = 'causas'

urlpatterns = [
    path('', views.Home_Causas, name="h_causas"),
    
]