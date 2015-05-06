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
def salvar(_resp,**propriedades):
	propriedades['categoria']=ndb.Key(Categoria,int(propriedades['categoria']))
	produto_form = validation.ProdutoForm(**propriedades)
	erros = produto_form.validate()
	if erros:
		_resp.set_status(400)
		# _resp.write(erros)
		return JsonUnsecureResponse(erros)
	else:
		# _resp.write('eba sem erro')
		produto = produto_form.fill_model()
		produto.put()
		contexto = produto_form.fill_with_model(produto)
		# _resp.write(contexto)
		return JsonUnsecureResponse(contexto) 
 