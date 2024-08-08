from odoo import api, fields, models

class SaleType(models.Model):
    _name = 'sale.type'

    name = fields.Char(string="Sale Type")
    is_rental = fields.Boolean()
    is_amc = fields.Boolean(string="Is AMC")
    note = fields.Html(string="Terms")