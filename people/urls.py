from django.urls import path

from .views import people_views as pv
from .views import animal_views as av

urlpatterns = [
	path('', pv.home, name="index"),
	path('listar/', pv.listar, name="listar"),
	path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),
	path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),
	path('cadastrar/', pv.cadastrar, name="cadastrar"),
	path('cadastro/', pv.cadastro, name="cadastro"),
	path('editar/<int:id_pessoa>/', pv.editar, name="editar"),
	path('update/<int:id_pessoa>/', pv.update, name="update"),
	# --------------------------------------------------------
	path('animal/cadastro/', av.cadastro, name="cadastro"),
	path('animal/cadastrar/', av.cadastrar, name="cadastrar"),
	path('animal/listar/', av.listar, name="listar"),
	path('animal/excluir/<int:id_animal>/', av.excluir, name="excluir"),
	path('animal/editar/<int:id_animal>/', av.editar, name="editar"),
	path('animal/update/<int:id_animal>/', av.update, name="update"),
]	