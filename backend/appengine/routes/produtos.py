from __future__ import absolute_import, unicode_literals

__author__ = 'william'
# -*- coding: utf-8 -*-
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from config.template_middleware import TemplateResponse


@login_not_required
@no_csrf
def index(__resp):
    __resp.write('teste')
    #return TemplateResponse()