from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    # INVOICING #

    def _prepare_invoice(self):
        values = super()._prepare_invoice()

        print("=============================")
        print("values before: ", values)
        print(self.client_no, self.client_dt)
        
        if self.client_no:
            values['client_no'] = self.client_no
        
        if self.client_dt:
            values['client_dt'] = self.client_dt
        
        if self.partner_invoice_id:
            values['partner_invoice_id'] = self.partner_invoice_id.id
        
        if self.sale_type_id:
            values['sale_type_id'] = self.sale_type_id.id

        if self.bank_id:
            values['bank_id'] = self.bank_id.id
        
        values['so_name'] = self.name
        values['date_order'] = self.date_order

        active_picking_id = self.picking_ids.filtered(
            lambda p: p.state == 'done'
        )[:1]

        if active_picking_id:
            values['dc_no'] = active_picking_id.name
            values['dc_dt'] = active_picking_id.date_done
        
        print("values after: ", values)
        print(self.picking_ids)
        print("active stock picking: ", active_picking_id)
        print("=============================")

        return values
    
    