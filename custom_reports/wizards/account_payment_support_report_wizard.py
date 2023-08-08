import time
import datetime
from urllib import response

from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.tools import float_is_zero
from odoo.tools import date_utils
import io
import json


class AccountPaymentSupportReportWizard(models.TransientModel):
    """ Account Payment Support Report Wizard """
    _name = 'account.payment.support.report.wizard'
    _description = "Account Payment Support Report"

    excel_file = fields.Binary('Excel Report')
    file_name = fields.Char('Excel File', size=64)

    @api.model
    def _get_current_date(self):
        """ :return current date """
        return fields.Date.today()

    start_date = fields.Date(string="Start Date", required=True, default=lambda self: self._get_current_date())
    end_date = fields.Date(string="End Date", required=True, default=lambda self: self._get_current_date())
    location_id = fields.Char(string="Shop")

    def generate_account_payment_support_excel_report(self):
        print("EXCEL REPORT TESTING")
        data = {}
        return self.env.ref('custom_reports.payment_support_excel_xlsx').report_action(self, data=data)
