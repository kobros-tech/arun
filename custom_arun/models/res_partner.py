# -*- coding: utf-8 -*-
# Part of kobros-tech. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class Partner(models.Model):
    _inherit = "res.partner"

    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    gstin_number = fields.Char(string='GSTIN Number')
    is_manufacturer = fields.Boolean()
    email = fields.Char(string='Email (O)')
    email_p = fields.Char(string='Email (P)')
    # website = fields.Char(copy=True)
    fax = fields.Char()

    def copy(self, default=None):
        self.ensure_one()
        chosen_name = default.get('name') if default else ''
        chosen_street = default.get('street') if default else ''
        new_name = chosen_name or _('%s (copy)', self.name)
        new_street = chosen_street or _('%s (copy)', self.street)
        default = dict(default or {}, name=new_name, street=new_street)

        return super(Partner, self).copy(default)

    @api.constrains('city', 'country_id', 'state_id', 'street', 'street2', 'zip')
    def _check_unique_address(self):
        for rec in self:
            if rec.is_company == True:
                existing_addresses = self.sudo().search([('is_company', '=', True)])
                
                if rec.country_id:
                    filtered_country = existing_addresses.filtered(lambda a: rec.country_id == a.country_id)
                    existing_addresses = filtered_country
                if rec.state_id:
                    filtered_state = existing_addresses.filtered(lambda a: rec.state_id == a.state_id)
                    existing_addresses = filtered_state
                if rec.city:
                    filtered_city = existing_addresses.filtered(lambda a: rec.city == a.city)
                    existing_addresses = filtered_city
                if rec.street:
                    filtered_street = existing_addresses.filtered(lambda a: rec.street == a.street)
                    existing_addresses = filtered_street
                if rec.street2:
                    filtered_street2 = existing_addresses.filtered(lambda a: rec.street2 == a.street2)
                    existing_addresses = filtered_street2
                if rec.zip:
                    filtered_zip = existing_addresses.filtered(lambda a: rec.zip == a.zip)
                    existing_addresses = filtered_zip

                if existing_addresses and len(existing_addresses) > 1 and rec in existing_addresses:
                    raise ValidationError(_('The same address is added for another company.'))
