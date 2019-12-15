"""este comentario es para solucionar el missing doc string..."""
from django.contrib import admin
from django.urls import path, include  
from .views import home, galeria, formulario, formulario2, login, login_iniciar, cerrar_sesion, eliminar_flor, agregar_carro, carrocompra


urlpatterns = [
    path('', home, name='HOME'),
    path('login/', login, name='LOGIN'),
    path('galeria/', galeria, name='GALERI'),
    path('formulario/', formulario2, name='FORMULA'),
    path('eliminar_flor/<id>/', eliminar_flor, name='ELIMINAR'),
    path('login_iniciar/', login_iniciar, name='LOGIN_INICIAR'),
    path('cerrar_sesion/', cerrar_sesion, name='CERRAR'),
    path('agregar_carro/<id>/', agregar_carro, name='A_CARRO'),
    path('carrocompra/', carrocompra, name='CARRO'),
    path('formulario/', formulario, name='FORMU'),


]
