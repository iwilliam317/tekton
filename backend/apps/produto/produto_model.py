# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property
from categoria.model import Categoria
from gaeforms.ndb.property import SimpleCurrency

class Produto(ndb.Model):
	nome = ndb.StringProperty(required=True)
	# FIX ME float não funciona
	preco = ndb.FloatProperty(required=True)
	categoria = ndb.KeyProperty(Categoria,required=True)
	descricao = ndb.StringProperty(required=True)
	novidade = ndb.StringProperty(required=True)
	#foto = ndb.StringProperty(required=True)

	@classmethod
	def query_ordenada_por_nome(cls):
		return cls.query().order(Produto.nome)

	@classmethod
	def query_por_categoria_ordenada_por_nome(cls, pesquisa_categoria):
		if isinstance(pesquisa_categoria, basestring):
			pesquisa_categoria=ndb.Key(Categoria, int(pesquisa_categoria))
		return cls.query(cls.categoria==pesquisa_categoria).order(cls.nome)