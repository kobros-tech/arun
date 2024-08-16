from odoo import api, fields, models, Command, _


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    manufacturer = fields.Many2one(
        "res.partner", 
        string="Manuf.",
        readonly=True,
    )
    commission_status = fields.Char(readonly=True,)
    hsn_code = fields.Char(
        string="HSN Code",
        related="product_id.hsn_code",
    )

