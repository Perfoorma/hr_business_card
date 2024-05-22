from odoo import fields, models, api


class EmployeeBusinessCard(models.Model):
    _inherit = "res.company"
    logo=fields.Binary()
    gif=fields.Binary()
