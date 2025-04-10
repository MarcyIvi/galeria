from django.urls import path
from .views import index
from django.urls import path
from . import views

urlpatterns = [
    path('', index, name='index'),  # URL para acessar a página inicial
    path('novo/', views.criar_personagem, name='criar_personagem'),
    path('personagens/', views.listar_personagens, name='listar_personagens'),
    path('sobre/', views.sobre_equipe, name='sobre_equipe'), # Página "Sobre a equipe"
]


