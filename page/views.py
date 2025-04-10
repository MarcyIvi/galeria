from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PersonagemForm
from .models import Personagem
from django.shortcuts import render
import os
from django.conf import settings

def index(request):
    return render(request, 'page/index.html')  # Renderiza o template

def criar_personagem(request):
    if request.method == 'POST':
        form = PersonagemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_personagens')
    else:
        form = PersonagemForm()
    return render(request, 'page/criar_personagem.html', {'form': form})

def listar_personagens(request):
    personagens = Personagem.objects.all()
    return render(request, 'page/listar_personagens.html', {'personagens': personagens})


def galeria(request):
    return render(request, 'page/index.html')


def sobre_equipe(request):
    return render(request, 'page/sobre_equipe.html')

