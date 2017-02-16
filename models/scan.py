# -*- coding: utf-8 -*-

from openerp import api, models, fields
import logging
_logger = logging.getLogger(__name__)

class Scan(models.Model):
    _name = 'ocr.scan'

    def run_scanner(self, cr, uid, ids, context=None, *args, **kwargs):
        try:
            import subprocess
            subprocess.Popen("date")
        except Exception as e:
            _logger.info("Could not scan: {} - {}".format(type(e), e.message))
        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }
