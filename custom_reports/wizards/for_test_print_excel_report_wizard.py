import time
import datetime
from urllib import response

from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.tools import float_is_zero
from odoo.tools import date_utils
import io
import json

try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class DamoExcelTestReports(models.TransientModel):
    _name = "damo.excel.test.report.wizard"
    _description = "Print Damo Excel Test Reports"

    data_from = fields.Date(string="From Data")
    data_to = fields.Date(string="To Data")
    report_ids = fields.Char(string="Reports IDS Name")

    def action_print_excel_report(self):
        print("EXCEL REPORT TESTING")
        data = {}
        return self.env.ref('custom_reports.report_damo_excel_xlsx').report_action(self, data=data)
