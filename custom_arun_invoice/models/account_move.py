# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, Command


class AccountMove(models.Model):
    _inherit = "account.move"

    partner_invoice_id = fields.Many2one(
        comodel_name='res.partner',
        string="Invoice Address",
        readonly=True,
        check_company=True,)
    sale_type_id = fields.Many2one(
        "sale.type",
        string="Sale Type",
        readonly=True,
    )
    so_name = fields.Char("Sale Order", readonly=True,)
    date_order = fields.Datetime(
        string="Order Date",
        readonly=True,
    )
    bank_id = fields.Many2one("res.bank", readonly=True,)
    dc_no = fields.Char(
        string="Delivery Challan",
        readonly=True,)
    dc_dt = fields.Datetime(
        string="Delivery Challan Date",
        readonly=True,)
    
    client_no = fields.Char(string="Client PO No.", readonly=True,)
    client_dt = fields.Date(string="Client PO Dt.", readonly=True,)
