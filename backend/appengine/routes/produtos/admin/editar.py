# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaepermission.decorator import login_required
from produto.produto_model import Produto
from categoria.model import Categoria
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes import categorias
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from produto import validation


@no_csrf
@login_required
def index(produto_id):
    produto = Produto.get_by_id(int(produto_id))
    contexto = {'produto': produto,
                'salvar_path': to_path(atualizar), 'acao': 'editar', 'categorias': Categoria.query_ordenada_por_nome()}
    return TemplateResponse(contexto, 'produtos/admin/cadastro.html')

@login_required
def atualizar(**propriedades):
    propriedades['categoria']=ndb.Key(Categoria,int(propriedades['categoria']))  
    produto_form = validation.ProdutoForm(**propriedades)
    erros = produto_form.validate()
    if erros:
        contexto = {'acao': 'atualizar', 'erros': erros, 'produto': produto_form,
                    'categorias': Categoria.query_ordenada_por_nome(), 'validacao_id' : Produto.get_by_id(int(propriedades['produto_id']))}
        return TemplateResponse(contexto, template_path='produtos/admin/cadastro.html')
    else:
        produto_id = propriedades['produto_id']
        produto = Produto.get_by_id(int(produto_id))
        produto.nome = propriedades['nome']
        produto.categoria = propriedades['categoria']
        produto.preco = float(propriedades['preco'])
        produto.descricao = propriedades['descricao']
        produto.novidade = propriedades['novidade']

        produto.put()
        return RedirectResponse('/produtos/admin')
