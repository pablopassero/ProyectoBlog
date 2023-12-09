from django.urls import path
from . import views

app_name = 'informacion'

urlpatterns = [
    path('', views.Home_Informacion, name="h_informacion"),
    
]