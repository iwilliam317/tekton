# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required



@login_not_required
@no_csrf
def index():

	### FIXME ENQUANTO NÃO TEM BD CRIAR CLASSE CENTRALIZADA PARA EVITAR REPLIUCAÇÃO DE CODIGO ###
	class Produto (object):
		def __init__(self, codigo, nome, descricao, preco, categoria, novidades):
			self.codigo = codigo
			self.descricao = descricao
			self.nome = nome
			self.preco = preco
			self.categoria = categoria
			self.novidades = novidades

	produtos = [Produto(1,'Roupa Sapinho', 'Roupa para Cachorro', 59.99, 'roupas',1), Produto(2,'Cama Onça', 'Cama para Cães e Gatos', 89.99, 'camas',0),Produto(3,'Coleira de Couro', 'Coleira para Cães', 59.99, 'coleiras',0),Produto(4,'Roupa Jard', 'Roupa para Cachorro', 79.99, 'roupas',1), Produto(5,'Camiseta Pug', 'Camiseta Unissex', 39.99, 'camisetas',0), Produto(6,'Camiseta Labrador', 'Camiseta Unissex', 39.99, 'camisetas',0), Produto(7,'Pedigree (Petisco)', 'Diversos Sabores', 9.99, 'alimentacao',1), Produto(8,'Ração Pedigree', 'Cachorros até 8kg', 19.99, 'alimentacao',0), Produto(9,'Caneca', 'Mosaico', 7.99, 'canecas',1), Produto(10,'Caneca', 'Chaplin', 7.99, 'canecas',0)]

	## somente as novidades aparecem na homepage | verificação por flag
	destaques = [x for x in produtos if x.novidades == 1]

	contexto = {'produtos' : destaques}
	return TemplateResponse(contexto)

