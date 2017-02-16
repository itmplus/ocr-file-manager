# -*- coding: utf-8 -*-
{
    'name': "OCR",

    'summary': """
        Manage Document File created from OCR""",

    'description': """
Document OCR and Management
========================================
* Run scheduled OCR action on directory containing images
* Search/filter documents by indexed keyword
""",

    'author': "IT Mplus 2017",
    'website': "http://www.example.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Document Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'external_dependencies': {
        'bin':['tesseract']
    },

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/document.xml',
        'views/scan.xml',
        'views/scheduler.xml',
        'views/path.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}