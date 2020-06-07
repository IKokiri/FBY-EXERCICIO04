from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from django.shortcuts import redirect

from ..models import Animal, AnimalEstimacao

def cadastro(request):
	template = loader.get_template('cadastro_animal.html')
	return HttpResponse(template.render({}, request))

def cadastrar(request):
    a = Animal(
        tipo=request.POST['tipo'],
        raca=request.POST['raca'],
        tamanho=request.POST['tamanho'],
    )
    a.save()
    return redirect('/people/animal/listar/')

@require_http_methods(["POST","GET"])
def listar(request):
    result = Animal.objects.all()
    template = loader.get_template('listar_animal.html')
    context = {
        'lista' : result,
    }
    return HttpResponse(template.render(context, request))

def excluir(request, id_animal):
	try:
		animal = Animal.objects.get(id=id_animal)
		animal.delete()		
		return redirect('/people/animal/listar/')
	except ObjectDoesNotExist:
		return HttpResponse("Animal não encontrado")


def editar(request, id_animal):
	try:
		animal = Animal.objects.get(id=id_animal)
		template = loader.get_template('editar_animal.html')
		context = {
			'animal' : animal,
		}
		return HttpResponse(template.render(context, request))
	except ObjectDoesNotExist:
		return HttpResponse("Animal não encontrado")


def update(request,id_animal):
	animal = Animal.objects.get(id=id_animal)
    
	animal.tipo = request.POST['tipo']
	animal.raca = request.POST['raca']
	animal.tamanho = request.POST['tamanho']
	animal.save()

	return redirect('/people/animal/listar/')

    
