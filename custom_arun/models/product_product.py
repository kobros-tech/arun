from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = "product.product"

    
    hsn_code = fields.Char(
        string="HSN Code",
        related="product_tmpl_id.hsn_code",
        readonly=False,
    )

    description= fields.Char(
        string="Description",
        related="product_tmpl_id.description",
        readonly=False,
    )

    manufacturer = fields.Many2one(
        "res.partner", 
        string="Manuf.",
        domain="[('is_manufacturer', '=', True)]",
        related="product_tmpl_id.manufacturer",
        readonly=False,
    )

    condition = fields.Many2one(
        'product.condition',
        string="Condition",
        related="product_tmpl_id.condition",
        readonly=False,
    )