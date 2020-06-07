from django.db import models

class Pessoa(models.Model):
	nome = models.CharField(max_length=200)
	idade = models.IntegerField(default=0)
	data_nascimento = models.DateField(null=True)
	cpf = models.CharField(max_length=14, null=True)

class Endereco(models.Model):
	pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	logradouro = models.CharField(max_length=200)
	numero = models.IntegerField()
	bairro = models.CharField(max_length=100,null=True)
	cep = models.CharField(max_length=9)

class Animal(models.Model):
	tipo = models.CharField(max_length=200)
	raca = models.CharField(max_length=200)
	tamanho = models.IntegerField()
	
class AnimalEstimacao(models.Model):
	animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null = True)
	pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null = True)
	nome = models.CharField(max_length=200)