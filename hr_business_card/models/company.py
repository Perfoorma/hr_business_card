from odoo import fields, models, api


class EmployeeBusinessCard(models.Model):
    _inherit = "res.company"
    bc_logo=fields.Binary()
    gif=fields.Binary()
