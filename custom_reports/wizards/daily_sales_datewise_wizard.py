import time
import datetime
from urllib import response

from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.tools import float_is_zero
from odoo.tools import date_utils
import io
import json


class DailySalesDatewiseWizard(models.TransientModel):
    """ Daily sales date wise report wizard """
    _name = 'daily.sales.datewise.wizard'
    _description = 'Daily Sales Date wise Report'

    @api.model
    def _get_current_date(self):
        """ :return current date """
        return fields.Date.today()

    start_date = fields.Date(required=True, default=lambda self: self._get_current_date())
    end_date = fields.Date(required=True, default=lambda self: self._get_current_date())
    store_zone_id = fields.Char(string="Territory")
    shop_loc_id = fields.Char(string='Shop')
    check = fields.Boolean(default=False)

    def daily_ales_date_wise_generate_report(self):
        print("EXCEL REPORT TESTING")
        data = {}
        return self.env.ref('custom_reports.daily_sales_datewise_excel_xlsx').report_action(self, data=data)
