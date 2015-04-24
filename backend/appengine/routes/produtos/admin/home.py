# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from produto.produto_model import Produto
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from categoria.model import Categoria
from tekton.router import to_path
from routes.produtos.admin import editar
from google.appengine.ext import ndb
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
@login_not_required
def index(_resp,categoria_selecionada=""):

    editar_path_base = to_path(editar)
    deletar_path_base = to_path(deletar)
    produtos = Produto.query().fetch()

    for prod in produtos:
        prod.editar_path = to_path(editar_path_base, prod.key.id())
        prod.deletar_path = to_path(deletar_path_base, prod.key.id())

    contexto = {'categorias':  Categoria.query()}


    if categoria_selecionada == "":
        contexto['produtos']=Produto.query_ordenada_por_nome().fetch()
        contexto['categoria_selecionada'] = None
    else:
        # sql = ndb.Key(Categoria, int(categoria_selecionada))
        # contexto['produtos']=Produto.query(Produto.categoria==sql).fetch()
        contexto['produtos']=Produto.query_por_categoria_ordenada_por_nome(categoria_selecionada).fetch()
        contexto['categoria_selecionada']=Categoria.get_by_id(int(categoria_selecionada))

    contexto['resultados'] = len(contexto['produtos'])   
    return TemplateResponse(contexto)
@login_not_required
def deletar(produto_id):
    
	produto= ndb.Key(Produto, int(produto_id))
	produto.delete()
	return RedirectResponse('/produtos/admin')