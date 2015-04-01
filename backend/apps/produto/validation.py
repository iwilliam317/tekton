# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from produto.produto_model import Produto


class ProdutoForm(ModelForm):
	_model_class = Produto
	_include = [Produto.nome, Produto.preco, Produto.categoria, Produto.descricao, Produto.novidade]
