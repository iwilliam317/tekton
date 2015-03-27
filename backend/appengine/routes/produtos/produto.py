# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index(p='1'):

	# class Produto (object):
	# 	def __init__(self, codigo, nome, descricao, preco):
	# 		self.codigo = codigo
	# 		self.descricao = descricao
	# 		self.nome = nome
	# 		self.preco = preco

	# produtos = [Produto(1,'Roupa Sapinho', 'Roupa para Cachorro', 59.90), Produto(2,'Cama Onça', 'Cama para Cães e Gatos', 89.90),Produto(3,'Coleira de Couro', 'Coleira para Cães', 59.90),Produto(4,'Roupa Jard', 'Roupa para Cachorro', 79.90), Produto(4,'Roupa Jard', 'Roupa para Cachorro', 79.90), Produto(1,'Roupa Sapinho', 'Roupa para Cachorro', 59.90),Produto(3,'Coleira de Couro', 'Coleira para Cães', 59.90)]

	# res = filter(lambda x: x.codigo == p, produtos)


	contexto= {'produto_id': p}
	return TemplateResponse(contexto,'/produtos/produto.html')

