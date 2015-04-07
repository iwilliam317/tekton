# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property
from categoria.model import Categoria

class Produto(Node):
	nome = ndb.StringProperty(required=True)
	# FIX ME float não funciona
	preco = ndb.StringProperty(required=True)
	# categoria = ndb.KeyProperty(Categoria,required=True)
	categoria = ndb.StringProperty(required=True)
	descricao = ndb.StringProperty(required=True)
	novidade = ndb.IntegerProperty(required=True)
	#foto = ndb.StringProperty(required=True)