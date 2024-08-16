from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    hsn_code = fields.Char(string="HSN Code")