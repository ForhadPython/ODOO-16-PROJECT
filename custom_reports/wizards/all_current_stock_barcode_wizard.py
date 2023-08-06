import time
import datetime
from urllib import response

from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.tools import float_is_zero
from odoo.tools import date_utils
import io
import json


class CurrentStockBarcodeReportWizard(models.TransientModel):
    """ Current Stock Barcode Report Wizard """
    _name = 'current.stock.barcode.report.wizard'
    _inherit = 'report.report_xlsx.abstract'
    _description = "Current Stock Barcode Report"

    excel_file = fields.Binary('Excel Report')
    file_name = fields.Char('Excel File', size=64)

    def current_stock_barcode_excel_report(self):
        print("EXCEL REPORT TESTING")
        data = {}
        return self.env.ref('custom_reports.report_all_current_stock_excel_xlsx').report_action(self, data=data)
