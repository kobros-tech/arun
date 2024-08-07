from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _compute_bank_domain(self):
        banks = self.env['res.partner.bank'].search([])
        print("============================")
        print(banks)
        print(self.partner_id.bank_ids)
        print(self.partner_id.bank_ids.ids)
        print("============================")
        
        return [('id', 'in', [1, 2, 3])]

    client_no = fields.Char(string="Client PO No.")
    client_dt = fields.Date(string="Client PO Dt.")
    sale_type_id = fields.Many2one(
        "sale.type",
        string="Sale Type",
    )

    bank_id = fields.Many2one(
        "res.partner.bank",
        string="Bank",
        domain="[('partner_id', '=', partner_id)]"
    )

    