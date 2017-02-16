# -*- coding: utf-8 -*-

from openerp import models, fields
import logging
_logger = logging.getLogger(__name__)

class Scheduler(models.Model):
    _name = 'ocr.scheduler'

    name = fields.Char(required=True)
    numberOfUpdates = fields.Integer('Number of updates',
                                     help='The number of times the scheduler has run and updated this field')
    lastModified = fields.Date('Last updated')

    def process_ocr_scheduler_queue(self, cr, uid, context=None):
        from PIL import Image
        import os, io
        _logger.info('..process_ocr_scheduler_queue is called.. ')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print('===CURR DIR=== ', dir_path)

        document_obj = self.pool.get('ocr.document')
        path_obj = self.pool.get('ocr.path')

        # process image files in each path
        for path_id in self.pool.get('ocr.path').search(cr, uid, []):
            path = path_obj.browse(cr, uid, path_id, context=context)
            print 'path: ', path_id, path
            dir_path = path.path
            for filename in os.listdir(dir_path):
                filename_fullpath = os.path.join(dir_path, filename)
                print filename_fullpath

                try:
                    # create document
                    curr_doc = document_obj.create(cr, uid, {
                        'name': filename,
                        'key': filename,
                        'type': 'binary'})

                    # run ocr on image
                    img = Image.open(filename_fullpath)
                    output = io.BytesIO()
                    img.save(output, format='JPEG')
                    bin_data = output.getvalue()
                    index_content = document_obj.browse(cr, uid, curr_doc).get_content(bin_data)
                    document_obj.write(cr, uid, curr_doc, {'index_content': index_content}, context=context)

                    os.remove(filename_fullpath)

                except Exception as e:
                    print "{} - {}".format(type(e), e.message)
