import base64
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


class MobileDataReportWizard(models.TransientModel):
    """ Mobile Data Report Wizard """
    _name = 'mobile.data.report.wizard'
    _description = "Mobile Data Report"

    def _get_current_date(self):
        """ :return current date """
        return fields.Date.today()

    start_date = fields.Date(string="Start Date", required=True, default=lambda self: self._get_current_date())
    end_date = fields.Date(string="End Date", required=True, default=lambda self: self._get_current_date())

    excel_file = fields.Binary('Excel Report')
    file_name = fields.Char(string='Excel File', size=64)

    @api.onchange('start_date')
    def _onchange_start_date(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            self.start_date = self.end_date

    @api.onchange('end_date')
    def _onchange_end_date(self):
        if self.end_date and self.end_date < self.start_date:
            self.start_date = self.end_date

    def generate_mobile_data_excel_report(self, data):
        """ Mobile Data Excel report object method """
        filename = 'Mobile Data Report'
        _inherit = 'report.report_xlsx.abstract'

        file_data = io.StringIO()

        workbook = xlsxwriter.Workbook(file_data)
        worksheet = workbook.add_worksheet()

        data = self.generate_mobile_data_report(data)

        self._excel_mobile_data_report(data, worksheet, workbook)

        workbook.close()
        file_data.seek(0)

        # with open(file_data, "r") as file:
        file_base64 = base64.b64encode(file_data.read())
        file_name = filename + '.xlsx'
        export_id = self.create({'excel_file': file_base64, 'file_name': file_name})

        return {
            'name': 'Mobile Data Report',
            'view_mode': 'form',
            'res_id': export_id.id,
            'res_model': 'mobile.data.report.wizard',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    def generate_mobile_data_report(self, data):
        """ Object Method """

        data['other'] = {
            'from_date': self.start_date,
            'to_date': self.end_date,
            'shop_name': self.location_id.name
        }
        return data

    @staticmethod
    def _excel_mobile_data_report(data, worksheet, workbook):
        """ Method to generate excel report for mobile data report """
        # Start Cell Style
        header_style_top = workbook.add_format(
            {'align': 'center', 'border': True, 'font_name': 'Arial', 'font_color': 'black', 'bold': True,
             'font_size': 18})
        header_style = workbook.add_format(
            {'align': 'center', 'border': True, 'font_name': 'Arial', 'font_color': 'black', 'bold': True,
             'font_size': 11})
        upper_header_style = workbook.add_format(
            {'align': 'center', 'border': True, 'font_name': 'Arial', 'font_color': 'black', 'bold': True,
             'font_size': 11})
        upper_header_style_left = workbook.add_format(
            {'align': 'left', 'border': True, 'font_name': 'Arial', 'font_color': 'black', 'bold': True,
             'font_size': 11})
        upper_header_style_right = workbook.add_format(
            {'align': 'right', 'border': True, 'font_name': 'Arial', 'font_color': 'black', 'bold': True,
             'font_size': 11})
        file_name_style = workbook.add_format({'bold': True})
        file_header_style = workbook.add_format({'font_name': 'Arial', 'font_color': 'black', 'bold': True})
        file_header_style_data = workbook.add_format({'font_name': 'Arial', 'font_color': 'black', 'align': 'left'})
        data_style_right = workbook.add_format({'font_name': 'Arial', 'font_color': 'black', 'align': 'right'})
        data_style_left = workbook.add_format({'font_name': 'Arial', 'font_color': 'black', 'align': 'left'})

        worksheet.merge_range(0, 0, 1, 5, "MOBILE DATA REPORT", header_style_top)
        for key, value in data.items():
            if key == 'other':
                worksheet.merge_range(0, 6, 0, 7, "FROM DATE:", file_header_style)
                worksheet.merge_range(0, 8, 0, 10, data[key]['from_date'], file_header_style_data)
                worksheet.merge_range(1, 6, 1, 7, "TO DATE:", file_header_style)
                worksheet.merge_range(1, 8, 1, 10, data[key]['to_date'], file_header_style_data)

        row = 3
        col = 0
        # Column Header
        worksheet.merge_range(row, col, row + 1, col, "SHOP CODE", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "INVOICE", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "MOBILE NO", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "MOBILE STATUS", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "ARTICLE CODE", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "PRODUCT CAT NAME", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "BRAND", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "SALE VALUE", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "DATE", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "TIME", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "MONTH", upper_header_style)

        row = 5
        # for key, values in data.items():
        #     if key == 'ids':
        #         for single_record in data[key]:
        #             col = 0
        #             worksheet.write(row, col, single_record['shop_code'], data_style_left)
        #             col = col + 1
        #             worksheet.write(row, col, single_record['invoice'], data_style_right)
        #             col = col + 1
        #             worksheet.write(row, col, single_record['mobile_no'], data_style_right)
        #             col = col + 1
        #             worksheet.write(row, col, single_record['mobile_status'], data_style_right)
        #             col = col + 1
        #             worksheet.write(row, col, single_record['article_code'], data_style_right)
        #             col = col + 1
        #             worksheet.write(row, col, single_record['prod_cat_name'], data_style_right)
        #             col = col + 1
        #             worksheet.write(row, col, single_record['brand'], data_style_right)
        #             col = col + 1
        #             worksheet.write(row, col, single_record['sale_val'], data_style_right)
        #             col = col + 1
        #             worksheet.write(row, col, single_record['date'], data_style_right)
        #             col = col + 1
        #             worksheet.write(row, col, single_record['time'], data_style_right)
        #             col = col + 1
        #             worksheet.write(row, col, single_record['month'], data_style_right)
        #
        #             row += 1
