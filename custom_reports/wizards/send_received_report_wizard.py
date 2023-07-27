import base64
import time
import datetime

from botocore.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.tools import float_is_zero
from odoo.tools import date_utils
import io
import json


class SendReceivedReportWizard(models.TransientModel):
    """ Send Received Report Wizard """
    _name = 'send.received.report.wizard'
    _description = "User Wise Sale Summary Report"

    excel_file = fields.Binary('Excel Report')
    file_name = fields.Char('Excel File', size=64)

    @api.model
    def _def_current_date(self):
        """:return current date"""
        return fields.Date.today()

    location_id = fields.Many2one(string="Shop")

    store_zone_id = fields.Many2one(string="Territory")
    article_id = fields.Many2one(string='Article', required=False, ondelete='cascade')
    down_to = fields.Float(string="Down To (%)", required=False, default='40')

    def generate_send_received_excel_report(self):
        print("EXCEL REPORT TESTING")
        data = {}
        return self.env.ref('custom_reports.report_mobile_data_excel_xlsx').report_action(self, data=data)
