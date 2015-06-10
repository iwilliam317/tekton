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
def index(_handler):
	upload_path = to_path(upload)
	bucket = get_default_gcs_bucket_name()
	url = blobstore.create_upload_url(upload_path, gs_bucket_name=bucket)
	contexto = {'upload_url' : url}

	return TemplateResponse(contexto)


@login_required
def upload(_handler, blob):
	blob_infos = _handler.get_uploads('blob')
	blob_facade.save_blob_files_cmd(blob_infos).execute()
	return RedirectResponse('/updown')
