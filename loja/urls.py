from django.urls import path    
from loja import views

app_name = 'loja'

urlpatterns = [
    path('', views.index, name='index'),
]
