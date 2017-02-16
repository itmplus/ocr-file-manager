# -*- coding: utf-8 -*-

from openerp import api, models, fields
import logging
import subprocess
from PIL import Image
from StringIO import StringIO

_logger = logging.getLogger(__name__)
_MARKER_PHRASE = '[[waiting for OCR]]'


class Document(models.Model):
    _name = 'ocr.document'
    _inherit = ['ir.attachment']

    key = fields.Char(required=True)
    content = fields.Text()
    path = fields.Char()


    def _index(self, cr, uid, bin_data):
        # dpi = int(
        #     self.env['ir.config_parameter'].get_param(
        #         'document_ocr.dpi', '500'))
        dpi = 300  # hardcode

        image_data = StringIO()
        try:
            Image.open(StringIO(bin_data)).save(image_data, 'tiff',
                                            dpi=(dpi, dpi))
        except IOError:
            _logger.exception('Failed to OCR image')
            return None

        process = subprocess.Popen(
            ['tesseract', 'stdin', 'stdout'],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate(image_data.getvalue())
        if stderr:
            _logger.info('Process OCR: %s', stderr)
        return stdout


    def _data_set(self, cr, uid, id, name, value, arg, context=None):
        return True

    def get_content(self, cr, uid, bin_data):
        print '..get_content called..'
        return self._index(cr, uid, bin_data)

