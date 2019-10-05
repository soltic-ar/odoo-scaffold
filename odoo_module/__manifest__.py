# -*- coding: utf-8 -*-
{
    'name': "odoo_module",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "SOLTic S.R.L.",
    'website': "https://www.soltic.com.ar",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list or ir_module_category table
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'external_dependencies': {'python': [], 'bin': []},
    'data': [
        ## Security
        # 'security/ir.model.access.csv',
        ## Views
        'views/views.xml',
        ## Menu
        # 'menu/...'
        ## Reports
        # 'reports/...'
        ## Wizards
        # 'wizards/...'
        ## Data
        'data/data.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
