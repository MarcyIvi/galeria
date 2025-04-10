from django.db import models

# Create your models here.

class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='personagens/')  # vai para media/personagens/

    def __str__(self):
        return self.nome
