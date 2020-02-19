# odoo-scaffold

## Scaffolding File Structure

```
soltic_odoo_module
├── controllers
│   ├── __init__.py
│   └── controllers.py
├── demo
│   └── demo.xml
├── models
│   ├── __init__.py
│   └── models.py
├── security
│   └── ir.model.access.csv
└── views
    ├── templates.xml
    └── views.xml
├── __init__.py
├── __manifest__.py
```

## Manifest

```xml
{
    'name': "soltic_odoo_module",
    'summary': """
        Summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'author': "SOLTic S.R.L., Odoo Community Association (OCA)",
    'website': "https://www.soltic.com.ar",
    'license': "LGPL-3",
    'category': 'Uncategorized',
    'version': '13.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
```
