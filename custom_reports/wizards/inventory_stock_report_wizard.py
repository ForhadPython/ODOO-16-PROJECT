import time
import datetime

from botocore.exceptions import ValidationError
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


class ExcelWizard(models.TransientModel):
    _name = "example.xlsx.wizard"

    source_loc_id = fields.Char('Store Location')
    product_cat_id = fields.Char(string="Category")
    calculate_transit = fields.Boolean('Calculate With Transit')

    def print_xlsx(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start Date must be less than End Date')
        data = {
            'source_loc_id': self.source_loc_id,
            'product_cat_id': self.product_cat_id,
        }
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'example.xlsx.wizard',
                     'options': json.dumps(data, default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Excel Report',
                     },
            'report_type': 'xlsx',
        }

    # def get_xlsx_report(self, data, response):
    #     from_date = data['source_loc_id']
    #     to_date = data['product_cat_id']
    #     output = io.BytesIO()
    #     workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    #     sheet = workbook.add_worksheet()
    #     cell_format = workbook.add_format(
    #         {'font_size': '12px', 'align': 'center'})
    #     head = workbook.add_format(
    #         {'align': 'center', 'bold': True, 'font_size': '20px'})
    #     txt = workbook.add_format({'font_size': '10px', 'align': 'center'})
    #     sheet.merge_range('B2:I3', 'EXCEL REPORT', head)
    #     sheet.merge_range('A6:B6', 'From Date:', cell_format)
    #     sheet.merge_range('C6:D6', from_date, txt)
    #     sheet.write('F6', 'To Date:', cell_format)
    #     sheet.merge_range('G6:H6', to_date, txt)
    #     workbook.close()
    #     output.seek(0)
    #     response.stream.write(output.read())
    #     output.close()
