# -*- coding: utf-8 -*-
# from odoo import http


# class SolticOdooModule(http.Controller):
#     @http.route('/soltic_odoo_module/soltic_odoo_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/soltic_odoo_module/soltic_odoo_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('soltic_odoo_module.listing', {
#             'root': '/soltic_odoo_module/soltic_odoo_module',
#             'objects': http.request.env['soltic_odoo_module.soltic_odoo_module'].search([]),
#         })

#     @http.route('/soltic_odoo_module/soltic_odoo_module/objects/<model("soltic_odoo_module.soltic_odoo_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('soltic_odoo_module.object', {
#             'object': obj
#         })
