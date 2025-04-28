from odoo import models


class ResCompany(models.Model):
    _inherit = "res.company"

    def action_send_mail_to_customer(self):
        """Send row material products to customers."""
        self._send_row_material_mail(
            template_xml_id="college_project.mail_template_row_material_info",
            partner_type="customer",
        )

    def action_send_mail_to_vendor(self):
        """Send row material products to vendors."""
        self._send_row_material_mail(
            template_xml_id="college_project.mail_template_row_material_info",
            partner_type="vendor",
        )

    def _send_row_material_mail(self, template_xml_id, partner_type):
        """Generic function to send row material products."""
        ProductTemplate = self.env["product.template"]
        Partner = self.env["res.partner"]

        products = ProductTemplate.search([("is_dairy_product", "=", True)])
        if not products:
            return

        product_data = [{
            "template_id": product.id,
            "name": product.name,
            "description": product.description_sale or product.name,
            "row_material_lines": [{
                "name": line.name,
                "quantity": line.quantity,
                "uom_name": line.uom_id.name,
                "standard_price": line.standard_price,
            } for line in product.row_matrial_line]
        } for product in products]

        # Find partners based on type
        domain = [
            ("company_id", "!=", self.id),
            ("type", "=", "contact"),
            ("active", "=", True),
        ]
        if partner_type == "customer":
            domain.append(("customer_rank", ">", 0))
        elif partner_type == "vendor":
            domain.append(("supplier_rank", ">", 0))

        partners = Partner.search(domain)
        if not partners:
            return

        template = self.env.ref(template_xml_id)

        for partner in partners:
            if not partner.email:
                continue  # Skip partners without email

            mail_template = template.with_context(
                recipient_name=partner.name,
                product_data=product_data,
            )

            # Set the real email on the mail template before sending
            mail_template.email_to = partner.email
            mail_template.send_mail(self.id, force_send=True)
