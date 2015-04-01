# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.model import Categoria
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from categoria import model
from tekton.router import to_path
from routes.categorias import editar


@no_csrf
def index():

    query = Categoria.query()

    editar_path_base = to_path(editar)
    deletar_path_base = to_path(deletar)

    categorias = query.fetch()
    for cat in categorias:
        cat.editar_path = to_path(editar_path_base, cat.key.id())
        cat.deletar_path = to_path(deletar_path_base, cat.key.id())

    contexto = {'categorias': categorias}
    return TemplateResponse(contexto)

def deletar(_resp,categoria_id):
    #query = Categoria.get_by_id(categoria_id)
    _resp.write(categoria_id)