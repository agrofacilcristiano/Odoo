# -*- coding: utf-8 -*-
# © 2009  Renato Lima - Akretion
# © 2016 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Brazilian Localisation ZIP Codes',
    'description': 'Brazilian Localisation ZIP Codes',
    'license': 'AGPL-3',
    'author': 'Akretion, Odoo Brasil',
    'version': '10.0.1.0.0',
    'depends': [
        'br_base',
    ],
    'data': [
        'views/l10n_br_zip_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'wizard/l10n_br_zip_search_view.xml',
        'security/ir.model.access.csv',
    ],
    'test': ['test/zip_demo.yml'],
    'category': 'Localization',
    'installable': True,
}