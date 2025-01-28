# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class clsu_brews_and_boards(models.Model):
#     _name = 'clsu_brews_and_boards.clsu_brews_and_boards'
#     _description = 'clsu_brews_and_boards.clsu_brews_and_boards'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

