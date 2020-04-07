# © 2019 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class WebsiteCookiebar(models.Model):

    _name = 'website.cookiebar'
    _description = 'Cookiebar'

    message = fields.Char(
        required=True,
        translate=True,
    )

    button_text = fields.Char(
        required=True,
        translate=True,
    )

    policy_text = fields.Char(
        string='Policy Link Text',
        translate=True,
    )

    policy_url = fields.Char(
        string='Policy URL',
    )
