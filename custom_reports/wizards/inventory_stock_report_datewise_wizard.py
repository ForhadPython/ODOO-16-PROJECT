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


class DateWiseInventoryStockReportWizard(models.TransientModel):
    """ Shop wise Stock statement report wizard """
    _name = 'inventory.stock.report.datewise.wizard'

    @api.model
    def _get_current_date(self):
        """ :return current date """
        return fields.Date.today()

    store_zone_id = fields.Char(string="Territory")
    source_loc_id = fields.Char('Store Location')
    start_date = fields.Date(default=lambda self: self._get_current_date(), required=True)
    end_date = fields.Date(default=lambda self: self._get_current_date(), required=True)
    product_cat_id = fields.Char(string="Category",
                                 help="Filter by parent category")
    is_packaging = fields.Selection([
        ('only_carry_bag', "Only Carry Bag"),
        ('without_carry_bag', "Without Carry Bag")
    ], string="Packaging")

    def action_inventory_stock_report(self):
        print("EXCEL REPORT TESTING")
        # data = {}
        # return self.env.ref('custom_reports.report_mobile_data_excel_xlsx').report_action(self, data=data)
