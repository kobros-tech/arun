from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    #=== BUSINESS METHODS ===#

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)

        print("=============================")
        print("values before: ", res)
        print(self.manufacturer)

        # if self.manufacturer:
        #     res['manufacturer'] = self.manufacturer.id
        
        if self.commission_status:
            res['commission_status'] = self.commission_status

        # if self.condition:
        #     res['condition'] = self.condition.id

        print("values after: ", res)
        print("=============================")

        return res
