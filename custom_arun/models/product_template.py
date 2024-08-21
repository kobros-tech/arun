from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    hsn_code = fields.Char(string="HSN Code")

    description= fields.Char(string="Description")

    manufacturer = fields.Many2one(
        "res.partner", 
        string="Manuf.",
        domain="[('is_manufacturer', '=', True)]"
    )

    condition = fields.Many2one(
        'product.condition',
        string="Condition",
    )
    