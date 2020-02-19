# -*- coding: utf-8 -*-
{
    'name': "soltic_odoo_module",

    'summary': """
        Summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'author': "SOLTic S.R.L., Odoo Community Association (OCA)",
    'website': "https://www.soltic.com.ar",
    'license': "LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
