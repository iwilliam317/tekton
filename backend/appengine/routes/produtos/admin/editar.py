# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from produto.produto_model import Produto
from categoria.model import Categoria

from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes import categorias
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path


@no_csrf
def index(produto_id):
    produto = Produto.get_by_id(int(produto_id))
    acao = 'editar'
    contexto = {'produto': produto,
           'salvar_path': to_path(atualizar),'erros': '', 'acao' : acao, 'categorias': Categoria.query_ordenada_por_nome()}
    return TemplateResponse(contexto, 'produtos/admin/cadastro.html')


def atualizar(produto_id, nome, categoria, descricao, preco, novidade):
    produto = Produto.get_by_id(int(produto_id))
    produto.nome = nome
    produto.categoria = categoria
    produto.preco = preco
    produto.descricao = descricao
    produto.novidade = int(novidade)

    produto.put()
    return RedirectResponse('/produtos/admin')
