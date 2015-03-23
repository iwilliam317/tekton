# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index():
    return TemplateResponse()

# @login_not_required
# @no_csrf
# def salvar(__resp, nome, email, senha, cpf, data_nascimento, sexo, telefone, celular = '', cep, endereco, numero, bairro, cidade, estado):
	##pegar parametros
	# nome = req.get('nome')
	# email = req.get('email')
	# senha = req.get('senha')
	# cpf = req.get('cpf')
	# data_nascimento = req.get('data_nascimento')
	# sexo = req.get('sexo')
	# telefone = req.get('telefone')
	# celular = req.get('celular')
	# cep = req.get('cep')
	# endereco = req.get('endereco')
	# numero = req.get('numero')
	# bairro = req.get('bairro')
	# cidade = req.get('cidade')
	# estado = req.get('estado')
	#__resp.write('sadad')