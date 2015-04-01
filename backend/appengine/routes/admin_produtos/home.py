# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from produto.produto_model import Produto
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
# from categoria import model
from tekton.router import to_path
from routes.admin_produtos import editar
from google.appengine.ext import ndb
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():

    query = Produto.query()

    editar_path_base = to_path(editar)
    deletar_path_base = to_path(deletar)

    produtos = query.fetch()
    for prod in produtos:
        prod.editar_path = to_path(editar_path_base, prod.key.id())
        prod.deletar_path = to_path(deletar_path_base, prod.key.id())


    contexto = {'produtos': produtos, 'resultados': len(produtos)}
    return TemplateResponse(contexto)

def deletar(produto_id):
	key= ndb.Key(Produto, int(produto_id))
	key.delete()
	return RedirectResponse('/admin_produtos')