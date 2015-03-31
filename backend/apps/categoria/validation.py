# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from categoria.model import Categoria

class CategoriaForm(ModelForm):
	_model_class = Categoria
	_include = [Categoria.nome, Categoria.categoria_pai]
