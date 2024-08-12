import datetime
from num2words import num2words
from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    client_no = fields.Char(string="Client PO No.")
    client_dt = fields.Date(string="Client PO Dt.")
    quote_subject = fields.Char(string="Quote Subject")
    sale_type_id = fields.Many2one(
        "sale.type",
        string="Sale Type",
    )

    bank_id = fields.Many2one("res.bank")

    def get_custom_name(self, report_type="SQ", state="draft"):
        x = datetime.datetime.now()
        y = datetime.datetime(2000, 1, 1)
        current_year = x.year - y.year
            
        SOs = self.env['sale.order'].sudo().search([('state', '=', state)])
        number = len(SOs) + 1

        # make SO sequence 5 places
        sequence = "%05d" % (number)
        new_SO_name = f"{report_type}-{current_year}-{sequence}"
        
        return new_SO_name


    #=== ONCHANGE METHODS ===#
    
    @api.onchange('sale_type_id')
    def _onchange_sale_type_id(self):
        for rec in self:
            if rec.sale_type_id and rec.sale_type_id.note:
                rec.note = rec.sale_type_id.note

    def amount_in_words(self, price):
        return num2words(price, to='cardinal')


    #=== CRUD METHODS ===#

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'company_id' in vals:
                self = self.with_company(vals['company_id'])
            if vals.get('name', _("New")) == _("New"):
                seq_date = fields.Datetime.context_timestamp(
                    self, fields.Datetime.to_datetime(vals['date_order'])
                ) if 'date_order' in vals else None
                vals['name'] = self.get_custom_name("SQ", "draft")

        return super().create(vals_list)

    
    #=== ACTION METHODS ===#
    
    def action_confirm(self):
        for rec in self:
            rec.name = self.get_custom_name("SO", "sale")

            return super().action_confirm()


    def action_draft(self):
        for rec in self:
            rec.name = self.get_custom_name("SQ", "draft")

            return super().action_draft()
    
    