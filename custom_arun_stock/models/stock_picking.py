# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Picking(models.Model):
    _inherit = "stock.picking"


    partner_0_id = fields.Many2one(
        comodel_name='res.partner',
        string="Partner",
        related="sale_id.partner_id",)
    partner_invoice_id = fields.Many2one(
        comodel_name='res.partner',
        string="Client Billing Address",
        related="sale_id.partner_invoice_id",)
    client_no = fields.Char(
        string="Client PO No.", 
        related="sale_id.client_no",)
    client_dt = fields.Date(
        string="Client PO Dt.", 
        related="sale_id.client_dt",)
    is_grn = fields.Boolean(string="Goods Receipt Note",)
    remarks = fields.Char(string="Remarks",)


    sale_type_id = fields.Many2one(
        "sale.type",
        string="Type of Transaction",
        related="sale_id.sale_type_id",)
    
    