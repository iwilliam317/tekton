# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.model import Categoria
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes import categorias
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path


@no_csrf
def index(categoria_id):
    categoria = Categoria.get_by_id(int(categoria_id))
    ctx = {'categoria': categoria,
           'salvar_path': to_path(atualizar),'erros': ''}
    return TemplateResponse(ctx, 'categorias/form.html')


def atualizar(categoria_id, nome, categoria_pai):
    categoria = Categoria.get_by_id(int(categoria_id))
    categoria.nome = nome
    categoria.categoria_pai = categoria_pai
    categoria.put()
    return RedirectResponse('/categorias')
