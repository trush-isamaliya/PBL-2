from odoo import models, fields


class RowMatrialLine(models.Model):
    _name = "row.matrial.line"
    _rec_name = "name"

    name = fields.Char(string="Name")
    product_temp_id = fields.Many2one("product.template", string="Product")
    quantity = fields.Integer(string="Quantity")
    uom_id = fields.Many2one("uom.uom", string="Unit of Measure")
    standard_price = fields.Float(string="Price")
