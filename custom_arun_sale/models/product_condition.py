from odoo import api, fields, models

class ProductCondition(models.Model):
    _name = 'product.condition'

    name = fields.Char()
    