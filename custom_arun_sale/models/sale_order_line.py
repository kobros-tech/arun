from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    description = fields.Char(
        string="Description",
        related="product_template_id.description",
        readonly=False,
    )

    manufacturer = fields.Many2one(
        "res.partner", 
        string="Manuf.",
        domain="[('is_manufacturer', '=', True)]",
        related="product_template_id.manufacturer",
        readonly=False,
    )

    commission_status = fields.Char(default="No commission agents")
    remark = fields.Char("Remarks")
    layout_category_id = fields.Many2one(
        'sale.layout_category',
        string="Section",
    )
    condition = fields.Many2one(
        'product.condition',
        string="Condition",
        related="product_template_id.condition",
        readonly=False,
    )
