from odoo import _, api, fields, models


class ResBank(models.Model):
    _inherit = 'res.bank'

    bic = fields.Char(string="Swift Code or BIC")
    ifsc_code = fields.Char(string="IFSC Code")
    cif_id = fields.Char(string="CIF ID")
    