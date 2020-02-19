# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class soltic_odoo_module(models.Model):
#     _name = 'soltic_odoo_module.soltic_odoo_module'
#     _description = 'soltic_odoo_module.soltic_odoo_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
