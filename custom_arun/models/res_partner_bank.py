from odoo import _, api, fields, models


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    street = fields.Char(
        related='bank_id.street',
        readonly=False,
    )
    street2 = fields.Char(
        related='bank_id.street2',
        readonly=False,
    )
    city = fields.Char(
        related='bank_id.city',
        readonly=False,
    )
    state = fields.Many2one(
        related='bank_id.state',
        readonly=False,
    )
    country = fields.Many2one(
        related='bank_id.country',
        readonly=False,
    )

    bic = fields.Char(
        related='bank_id.bic',
        readonly=False,
    )

    ifsc_code = fields.Char(
        related='bank_id.ifsc_code',
        readonly=False,
    )

    cif_id = fields.Char(
        related='bank_id.cif_id',
        readonly=False,
    )

    phone = fields.Char(
        related='bank_id.phone',
        readonly=False,
    )

    email = fields.Char(
        related='bank_id.email',
        readonly=False,
    )

    active = fields.Boolean(default=True)