import time
import datetime
from urllib import response

from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.tools import float_is_zero
from odoo.tools import date_utils
import io
import json


class RecapHOReportWizard(models.TransientModel):
    """ Recap HO report wizard."""
    _name = 'recap.shop.report.wizard'
    _description = "Recap Shop Report"

    @api.model
    def _get_current_date(self):
        """ :return current date """
        return fields.Date.today()

    store_zone_id = fields.Char(string="Territory")
    location_id = fields.Char(string='Store Location')
    from_date = fields.Date(default=lambda self: self._get_current_date(), required=True)
    to_date = fields.Date(default=lambda self: self._get_current_date(), required=True)
    old_gura_claim_show = fields.Boolean(string="Old Guarantee and Claim show", default=False)

    adjustment_show = fields.Boolean(string="Adjustment Show", default=False)

    def action_recap_shop_report(self):
        print("EXCEL REPORT TESTING")
        data = {}
        return self.env.ref('custom_reports.recap_shop_report_excel_xlsx').report_action(self, data=data)
