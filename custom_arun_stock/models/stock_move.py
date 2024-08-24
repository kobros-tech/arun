# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class StockMove(models.Model):
    _inherit = "stock.move"


    product_id = fields.Many2one(string="Part No.",)
    
    description0 = fields.Char(
        string="Description",
        related="product_id.description0",)

    manufacturer = fields.Many2one(
        comodel_name='res.partner',
        string="Manf.",
        related="product_id.manufacturer",)
    
    hsn_code = fields.Char(
        string="HSN Code",
        related="product_id.hsn_code",
    )

    condition = fields.Many2one(
        'product.condition',
        string="Condition",
        related="product_id.condition",
    )
    
    