# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property

class Categoria(Node):
	nome = ndb.StringProperty(required=True)
	categoria_pai = ndb.StringProperty(required=True)
	
	@classmethod
	def query_ordenada_por_nome(cls):
		return cls.query().order(Categoria.nome)