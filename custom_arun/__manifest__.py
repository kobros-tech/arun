# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#############################################################################
#
#    kobros-tech Pvt. Ltd.
#
#    Copyright (C) 2020-TODAY kobros-tech(<https://www.linkedin.com/company/kobros-tech/>).
#    Author: Mohamed Alkobrosli(<https://www.linkedin.com/in/mohamed-alkobrosly/>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': "Custom module Mr. Arun",
    'description': """
        Custom module Mr. Arun
    """,
    'author': 'Abou Sajid (Mohamed Alkobrosli)',
    'company': 'kobros-tech',
    'maintainer': 'Mohamed Moustafa Alkobrosli',
    'website': "https://www.kobros-tech.com",
    'license': "AGPL-3",
    'depends': [
        'base', 
        'contacts',
        'product',
        'purchase',
        'crm',
    ],
    'data': [
        "security/ir.model.access.csv",
        
        "views/res_partner_views.xml",
        "views/res_bank_views.xml",
        "views/product_template_views.xml",

        "report/purchase_reports.xml",
    ],
}
