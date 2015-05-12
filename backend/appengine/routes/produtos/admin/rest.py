# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required
from produto import validation
from google.appengine.ext import ndb
from categoria.model import Categoria
from produto.produto_model import Produto
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse

@login_required
@no_csrf
def listar():
	produtos=Produto.query().fetch()
	produto_form = validation.ProdutoForm()
	produtos = [produto_form.fill_with_model(p) for p in produtos]

	return JsonUnsecureResponse(produtos)

@login_required
@no_csrf
def salvar(_resp,**propriedades):
	propriedades['categoria']=ndb.Key(Categoria,int(propriedades['categoria']))
	produto_form = validation.ProdutoForm(**propriedades)
	erros = produto_form.validate()
	if erros:
		_resp.set_status(400)

		return JsonUnsecureResponse(erros)
	else:
		produto = produto_form.fill_model()
		produto.put()
		contexto = produto_form.fill_with_model(produto)

		return JsonUnsecureResponse(contexto) 
 

@login_required
@no_csrf
def deletar(produto_id):
	key = ndb.Key(Produto, int(produto_id))

	key.delete()
