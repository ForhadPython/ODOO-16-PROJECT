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

    location_id = fields.Char(string="Shop")

    store_zone_id = fields.Char(string="Territory")
    article_id = fields.Char(string='Article', required=False)
    down_to = fields.Float(string="Down To (%)", required=False, default='40')

    def generate_send_received_excel_report(self):
        print("EXCEL REPORT TESTING")
        data = {}
        return self.env.ref('custom_reports.report_mobile_data_excel_xlsx').report_action(self, data=data)
