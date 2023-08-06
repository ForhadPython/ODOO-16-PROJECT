import time
import datetime
from urllib import response

from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.tools import float_is_zero
from odoo.tools import date_utils
import io
import json


class PointReportWizard(models.TransientModel):
    """ Salesman Wise Sales Summary Report Wizard """
    _name = 'point.report.wizard'
    _description = "Point Report"

    excel_file = fields.Binary('Excel Report')
    file_name = fields.Char('Excel File', size=64)

    @api.model
    def _get_current_date(self):
        """ :return current date """
        return fields.Date.today()

    start_date = fields.Date(string="Start Date", default=lambda self: self._get_current_date())
    end_date = fields.Date(string="End Date", default=lambda self: self._get_current_date())
    location_id = fields.Char(string="Shop")
    sales_man_wise = fields.Boolean(string="Salesman Wise", default=False)

    team_name = fields.Selection(
        [
            ('pentagon', "PENTAGON"),
            ('challenger', "CHALLENGER"),
            ('fighter', "FIGHTER"),
            ('warriors', "WARRIORS"),
            ('defender', "DEFENDER"),
            ('survivor', "SURVIVOR"),
        ], string="Team")

    def generate_point_excel_report(self):
        print("EXCEL REPORT TESTING")
        data = {}
        return self.env.ref('custom_reports.report_all_current_stock_excel_xlsx').report_action(self, data=data)
