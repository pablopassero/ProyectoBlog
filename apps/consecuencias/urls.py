from django.urls import path
from . import views

app_name = 'consecuencias'

urlpatterns = [
    path('', views.Home_Consecuencias, name="h_consecuencias"),
    
]