# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router
from categoria import model
from categoria import validation

from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    contexto = {'salvar_path': router.to_path(salvar), 'categoria': '', 'erros': '',  'acao': 'adicionar'}
    return TemplateResponse(contexto, template_path='categorias/form.html')


def salvar(_resp, **propriedades):
    categoria_form = validation.CategoriaForm(**propriedades)
    erros = categoria_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar), 'erros': erros, 'categoria': categoria_form}
        return TemplateResponse(contexto, template_path='categorias/form.html')
    else:
        # categoria = validation.CategoriaForm.fill_model()
        categoria = model.Categoria(nome=propriedades['nome'], categoria_pai=propriedades['categoria_pai'])
        categoria.put()
        return RedirectResponse('/categorias')

