from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_row_matrial_customer = fields.Boolean(
        string="Is Row Matrial Customer?", copy=False
    )
    is_row_matrial_vendor = fields.Boolean(string="Is Row Matrial Vendor?", copy=False)
