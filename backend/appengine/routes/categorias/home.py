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


@no_csrf
@login_required
def index():

    query = Categoria.query()

    editar_path_base = to_path(editar)
    deletar_path_base = to_path(deletar)

    categorias = query.fetch()
    for cat in categorias:
        cat.editar_path = to_path(editar_path_base, cat.key.id())
        cat.deletar_path = to_path(deletar_path_base, cat.key.id())


    contexto = {'categorias': categorias, 'resultados': len(categorias)}
    return TemplateResponse(contexto)

@login_required
def deletar(_resp,categoria_id):
	key= ndb.Key(Categoria, int(categoria_id))
	key.delete()
	return RedirectResponse('/categorias')