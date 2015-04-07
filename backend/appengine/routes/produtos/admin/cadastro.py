# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.model import Categoria
from produto.produto_model import Produto
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from produto import validation
from tekton.router import to_path

from google.appengine.ext import ndb
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    salvar_path = to_path(salvar)
    contexto = {'categorias': Categoria.query_ordenada_por_nome(), 'salvar_path': salvar_path, 'erros': '', 'produto': '', 'acao' : 'adicionar'}
    return TemplateResponse(contexto)


def salvar(_resp, **propriedades):
    produto_form = validation.ProdutoForm(**propriedades)
    erros = produto_form.validate()

    if erros:
        contexto = {'salvar_path': to_path(salvar), 'erros': erros, 'produto': produto_form , 'categorias' : Categoria.query_ordenada_por_nome()}
        return TemplateResponse(contexto, template_path='produtos/admin/cadastro.html')
    else:    	
        #produto = validation.ProdutoForm.fill_model()
        produto = Produto(nome=propriedades['nome'], preco=propriedades['preco'], categoria=propriedades['categoria'], descricao = propriedades['descricao'], novidade = int(propriedades['novidade']))
        produto.put()
        return RedirectResponse('/produtos/admin')