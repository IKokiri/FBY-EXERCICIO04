from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from django.shortcuts import redirect

from ..models import Pessoa, Endereco,Animal,AnimalEstimacao

@require_http_methods(["GET","POST"])
def home(request):
	template = loader.get_template('inicio.html')
	return HttpResponse(template.render())
	
@require_http_methods(["POST","GET"])
def listar(request):
	result = Pessoa.objects.all()
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def detalhar(request, id_pessoa):
	try:
		pessoa = Pessoa.objects.get(id=id_pessoa)
		return HttpResponse(f"Detalhou {pessoa.nome} (id={pessoa.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Pessoa não encontrada")

def excluir(request, id_pessoa):
	try:
		pessoa = Pessoa.objects.get(id=id_pessoa)
		pessoa.delete()		
		return redirect('/people/listar/')
	except ObjectDoesNotExist:
		return HttpResponse("Pessoa não encontrada")

def cadastrar(request):
	dtn = datetime.strptime(request.POST['nascimento'], "%d/%m/%Y").date()
	p = Pessoa(
		nome=request.POST['nome'],
		idade=request.POST['idade'],
		data_nascimento=dtn,
		cpf=request.POST['cpf'],
	)
	
	e = Endereco(
		pessoa = p,
		logradouro = request.POST['logradouro'],
		numero = request.POST['numero'],
		bairro = request.POST['bairro'],
		cep = request.POST['cep'],
	)
	p.save()
	e.save()
	an = Animal.objects.get(id=request.POST['animal'])
	nome_animal = request.POST['nome_animal']
	
	ae = AnimalEstimacao(
		animal = an,
		pessoa = p,
		nome = nome_animal,
	)
	ae.save()
	return redirect('/people/listar/')

def cadastro(request):
	template = loader.get_template('cadastro.html')
	animais = Animal.objects.all()
	context = {
		'animais' : animais,
	}
	return HttpResponse(template.render(context, request))

def editar(request, id_pessoa):
	try:
		pessoa = Pessoa.objects.get(id=id_pessoa)
		pessoa.data_nascimento = pessoa.data_nascimento.strftime("%d/%m/%Y")
		endereco = Endereco.objects.get(pessoa=pessoa)
		template = loader.get_template('editar.html')
		animais = Animal.objects.all()
		ae = AnimalEstimacao.objects.get(pessoa=pessoa)
		
		context = {
			'pessoa' : pessoa,
			'endereco': endereco,
			'animais': animais,
			'animal': ae
		}
		return HttpResponse(template.render(context, request))
	except ObjectDoesNotExist:
		return HttpResponse("Pessoa não encontrada")

def update(request,id_pessoa):
	pessoa = Pessoa.objects.get(id=id_pessoa)

	dtn = datetime.strptime(request.POST['nascimento'], "%d/%m/%Y").date()
	pessoa.nome = request.POST['nome']
	pessoa.idade = request.POST['idade']
	pessoa.data_nascimento = dtn
	pessoa.cpf = request.POST['cpf']
	pessoa.save()

	end = Endereco.objects.get(pessoa=pessoa)
	end.logradouro = request.POST['logradouro']
	end.numero = request.POST['numero']
	end.bairro = request.POST['bairro']
	end.cep = request.POST['cep']

	ae = AnimalEstimacao.objects.get(pessoa=pessoa)
	ae.nome = request.POST['nome_animal']
	ae.animal_id = request.POST['animal']
	ae.save()

	end.save()

	return redirect('/people/listar/')
		
		