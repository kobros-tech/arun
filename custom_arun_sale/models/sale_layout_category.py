from odoo import api, fields, models

class SaleLayoutCategory(models.Model):
    _name = 'sale.layout_category'

    name = fields.Char()
    