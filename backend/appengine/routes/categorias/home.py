# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from categoria import model


@no_csrf
def index():
	query = model.Categoria.query()
	query.fetch()

	contexto = {'lista_categorias' : query.fetch()}
	return TemplateResponse(contexto)

