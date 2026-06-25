from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaInicial, name='pagina_inicial'),
    path('cadastrar/', views.cadastrarcliente, name='cadastrar_cliente'), # Rota do ENVIO
    path('cadastrar/', views.cadastrarcliente, name='cadastrar_cliente'),
    path('editar/<int:cliid>/', views.editar, name='editar'),
    path('editarcliente/', views.editarcliente, name='editar_cliente'),
    path('remover/<int:cliid>/', views.remover, name='remover'),
]