from django.urls import path
from . import views

app_name = 'solucion'

urlpatterns = [
    path('', views.Home_Solucion, name="h_solucion"),
    
]