from num2words import num2words
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    client_no = fields.Char(string="Client PO No.")
    client_dt = fields.Date(string="Client PO Dt.")
    sale_type_id = fields.Many2one(
        "sale.type",
        string="Sale Type",
    )

    bank_id = fields.Many2one("res.bank")


    @api.onchange('sale_type_id')
    def _onchange_sale_type_id(self):
        for rec in self:
            if rec.sale_type_id and rec.sale_type_id.note:
                rec.note = rec.sale_type_id.note

    def amount_in_words(self, price):
        return num2words(price, to='cardinal')
    