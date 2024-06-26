from odoo import fields, models, api

try:
  import qrcode
except ImportError:
  qrcode = None
try:
  import base64
except ImportError:
  base64 = None
from io import BytesIO

class EmployeeBusinessCard(models.Model):
    _inherit = "hr.employee"

    enable_business_card=fields.Boolean(string="Enable Business Card", default=False, groups="hr.group_hr_user")
    gif=fields.Binary(groups="hr.group_hr_user")
    linkedin=fields.Char(groups="hr.group_hr_user")
    url=fields.Char(string="Business Card URL", compute="_url", groups="hr.group_hr_user",store="True")
    bcFirstname=fields.Char(string="First Name", groups="hr.group_hr_user")
    bcLastname=fields.Char(string="Last Name", groups="hr.group_hr_user")
    qr_code=fields.Binary("QR Code", compute='_generate_qr_code', groups="hr.group_hr_user")


    @api.depends("url")
    def _generate_qr_code(self):
        for rec in self:
           if qrcode and base64:
               qr = qrcode.QRCode(version=1, box_size=10, border=4, error_correction=qrcode.constants.ERROR_CORRECT_L)
               qr.add_data(self.url)
               qr.make(fit=True)
               img = qr.make_image(fill_color="black", back_color="white")
               temp = BytesIO()
               img.save(temp, format="PNG")
               qr_image = base64.b64encode(temp.getvalue())
               rec.update({'qr_code': qr_image})

    @api.depends("enable_business_card")
    def _url(self):
        for record in self:
            record.url=self.env['ir.config_parameter'].sudo().get_param('web.base.url').rstrip('/')+"/business-card?employee="+str(record.id)
