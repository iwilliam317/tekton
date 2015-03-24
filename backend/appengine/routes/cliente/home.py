# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index(_resp,nome='a'):
    #return TemplateResponse()
    _resp.write(nome)


# @login_not_required
# @no_csrf
# def cadastro():
#     return TemplateResponse()
