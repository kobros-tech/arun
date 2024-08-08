from odoo import _, api, fields, models


class ResBank(models.Model):
    _inherit = 'res.bank'

    acc_holder_name = fields.Char(string="Account Holder Name")
    acc_number = fields.Char(string="Account Number")

    bic = fields.Char(string="Swift Code or BIC")
    ifsc_code = fields.Char(string="IFSC Code")
    cif_id = fields.Char(string="CIF ID")
    