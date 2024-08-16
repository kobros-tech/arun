from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = "product.product"

    hsn_code = fields.Char(
        string="HSN Code",
        related="product_tmpl_id.hsn_code",
    )