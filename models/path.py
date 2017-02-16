# -*- coding: utf-8 -*-

from openerp import models, fields
import logging
_logger = logging.getLogger(__name__)

class Path(models.Model):
    _name = 'ocr.path'

    name = fields.Char()
    path = fields.Char()

