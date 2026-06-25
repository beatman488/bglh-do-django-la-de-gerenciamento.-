from django.db import models

# Modelo de Categorias
class Categorias(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


# Modelo de Clientes (Adicionado para o seu sistema de gerenciamento)
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome