# -*- coding: utf-8 -*-
# Part of kobros-tech. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class Partner(models.Model):
    _inherit = "res.partner"

    gstin_number = fields.Char(string='GSTIN Number')
    is_manufacturer = fields.Boolean()
    email = fields.Char(string='Email (O)')
    email_p = fields.Char(string='Email (P)')
    fax = fields.Char()
