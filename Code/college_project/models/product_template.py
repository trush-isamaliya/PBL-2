from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_dairy_product = fields.Boolean(string="Is Dairy Product?", copy=False)
    is_row_matrial = fields.Boolean(string="Is Row Matrial?", copy=False)
    row_matrial_line = fields.One2many("row.matrial.line", "product_temp_id")
