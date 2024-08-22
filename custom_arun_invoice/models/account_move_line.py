from odoo import api, fields, models, Command, _


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    description = fields.Char(
        string="Description",
        related="product_id.description",
        readonly=True,
    )
    manufacturer = fields.Many2one(
        "res.partner", 
        string="Manuf.",
        related="product_id.manufacturer",
        readonly=True,
    )
    commission_status = fields.Char(readonly=True,)
    hsn_code = fields.Char(
        string="HSN Code",
        related="product_id.hsn_code",
        readonly=True,
    )
    condition = fields.Many2one(
        'product.condition',
        string="Condition",
        related="product_id.condition",
        readonly=True,
    )

