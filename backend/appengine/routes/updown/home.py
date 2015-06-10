# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton.gae.middleware.redirect import RedirectResponse
from gaepermission.decorator import login_required
from gaecookie.decorator import no_csrf
from tekton.router import to_path
from google.appengine.ext import blobstore
from blob_app import blob_facade
from google.appengine.api.app_identity.app_identity import get_default_gcs_bucket_name


@login_required
@no_csrf
def index():
	comando=blob_facade.list_blob_files_cmd()
	arquivos=comando()
	download_path=to_path(download)
	for arq in arquivos:
		arq.download_path=to_path(download_path,arq.key.id(),arq.filename)
	ctx={'arquivos':arquivos}
	return TemplateResponse(ctx)

@login_required
@no_csrf
def download(_handler,id,filename):
	comando=blob_facade.get_blob_file_cmd(id)
	arquivo=comando()
	_handler.send_blob(arquivo.blob_key)
