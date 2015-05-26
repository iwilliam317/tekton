# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.model import Categoria
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required
from categoria import model
from tekton.router import to_path
from routes.categorias import editar
from google.appengine.ext import ndb
from tekton.gae.middleware.redirect import RedirectResponse
from routes.categorias import rest
from categoria import validation
import json


@no_csrf
@login_required
def index(_resp):
    categorias = Categoria.query().fetch()
    categoria_form = validation.CategoriaForm()

    categorias = [categoria_form.fill_with_model(c) for c in categorias]

    # str_json = json.dumps(categorias)


    contexto = {'rest_salvar_path': to_path(rest.salvar), 'rest_listar_path' : to_path(rest.index), 'resultados': len(categorias)}
    return TemplateResponse(contexto)

@login_required
def deletar(_resp,categoria_id):
	key= ndb.Key(Categoria, int(categoria_id))
	key.delete()
	return RedirectResponse('/categorias')