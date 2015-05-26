# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required
from categoria import validation
from google.appengine.ext import ndb
from categoria.model import Categoria
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse

@login_required
@no_csrf
def salvar(_resp,**propriedades):
	categoria_form = validation.CategoriaForm(**propriedades)
	erros = categoria_form.validate()
	if erros:
		_resp.set_status(400)

		return JsonUnsecureResponse(erros)
	else:
		categoria = categoria_form.fill_model()
		categoria.put()
		contexto = categoria_form.fill_with_model(categoria)

		return JsonUnsecureResponse(contexto) 

@login_required
@no_csrf
def index():
	categorias = Categoria.query().fetch()
	categoria_form = validation.CategoriaForm()
	categorias = [categoria_form.fill_with_model(c) for c in categorias]
	return JsonUnsecureResponse(categorias)




