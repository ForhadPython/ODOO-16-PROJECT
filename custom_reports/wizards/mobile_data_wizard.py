import time
import datetime
from urllib import response

from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.tools import float_is_zero
from odoo.tools import date_utils
import io
import json


class MobileDataReportWizard(models.TransientModel):
    """ Mobile Data Report Wizard """
    _name = 'mobile.data.report.wizard'
    _description = "Mobile Data Report"

    excel_file = fields.Binary('Excel Report')
    file_name = fields.Char('Excel File', size=64)

    def _get_current_date(self):
        """ :return current date """
        return fields.Date.today()

    data_from = fields.Date(required=True, default=lambda self: self._get_current_date())
    data_to = fields.Date(required=True, default=lambda self: self._get_current_date())
    report_ids = fields.Char(string="Reports IDS Name")

    def action_print_mobile_data_excel_report(self):
        print("EXCEL REPORT TESTING")
        data = {}
        return self.env.ref('custom_reports.report_mobile_data_excel_xlsx').report_action(self, data=data)
