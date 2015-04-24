# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaepermission.decorator import login_not_required
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
@login_not_required
def index(produto_id):
    produto = Produto.get_by_id(int(produto_id))
    contexto = {'produto': produto,
                'salvar_path': to_path(atualizar), 'acao': 'editar', 'categorias': Categoria.query_ordenada_por_nome()}
    return TemplateResponse(contexto, 'produtos/admin/cadastro.html')

@login_not_required
def atualizar(**propriedades):
    produto_form = validation.ProdutoForm(**propriedades)
    erros = produto_form.validate()
    if erros:
        ############# FIX-ME, PERDENDO O ID QUANDO OCORRE ERRO NA VALIDAÇÃO###########
        contexto = {'acao': 'atualizar', 'erros': erros, 'produto_form': produto_form,
                    'categorias': Categoria.query_ordenada_por_nome(), 'produto': propriedades['produto_id']}
        return TemplateResponse(contexto, template_path='produtos/admin/cadastro.html')
    else:
        produto_id = propriedades['produto_id']
        produto = Produto.get_by_id(int(produto_id))
        produto.nome = propriedades['nome']
        produto.categoria = ndb.Key(Categoria, int(propriedades['categoria']))
        produto.preco = int(propriedades['preco'])
        produto.descricao = propriedades['descricao']
        produto.novidade = propriedades['novidade']

        produto.put()
        return RedirectResponse('/produtos/admin')
