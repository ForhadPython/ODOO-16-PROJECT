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

try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class FootNonFootWiseWizard(models.TransientModel):
    _name = 'foot.nonfoot.report.wizard'
    _description = 'Footwear Non-footwear Sales Report'

    excel_file = fields.Binary('Excel Report')
    file_name = fields.Char('Excel File', size=64)

    def _get_current_date(self):
        """ :return current date """
        return fields.Date.today()

    start_date = fields.Date(required=True, default=lambda self: self._get_current_date())
    end_date = fields.Date(required=True, default=lambda self: self._get_current_date())
    shop_loc_id = fields.Char(string="Shop Name")

    @api.onchange('start_date')
    def _onchange_start_date(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            self.end_date = self.start_date

    @api.onchange('end_date')
    def _onchange_end_date(self):
        if self.end_date and self.end_date < self.start_date:
            self.start_date = self.end_date

    def action_generate_excel_report(self, data):
        """ Footwear and non Footwear Excel report object method """
        filename = 'Footwear and Non Footwear Report'

        file_data = io.StringIO()

        workbook = xlsxwriter.Workbook(file_data)
        worksheet = workbook.add_worksheet()
        data['other'] = {
            'date_start': self.start_date,
            'date_stop': self.end_date,
            'shop_loc_id': self.stock_loc_id,
        }

        self._excel_plot_for_foot_and_nonfoot_report(data, worksheet, workbook)

        workbook.close()
        file_data.seek(0)

        file_base64 = base64.b64encode(file_data.read())
        file_name = filename + '.xlsx'
        export_id = self.write({'excel_file': file_base64, 'file_name': file_name})

        return {
            'name': 'Foot Nonfoot Report',
            'view_mode': 'form',
            'res_id': self.id,
            # 'res_model': 'foot.nonfoot.report.wizard',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    def _excel_plot_for_foot_and_nonfoot_report(data, worksheet, workbook):
        """ Method to generate excel report for shop wise stock report """
        # Start Cell Styl
        header_style_top = workbook.add_format(
            {'align': 'center', 'border': True, 'font_name': 'Arial', 'font_color': 'black', 'bold': True,
             'font_size': 17})
        header_style = workbook.add_format(
            {'align': 'center', 'border': True, 'bold': True, 'font_name': 'Arial', 'font_color': 'black',
             'font_size': 11})
        header_style_sale_qty = workbook.add_format(
            {'align': 'center', 'border': True, 'bold': True, 'font_name': 'Arial', 'font_color': 'black',
             'font_size': 11})
        header_style_amount = workbook.add_format(
            {'align': 'center', 'border': True, 'bold': True, 'font_name': 'Arial', 'font_color': 'black',
             'font_size': 11})
        file_header_style = workbook.add_format(
            {'font_name': 'Arial', 'font_color': 'black', 'bold': True})
        file_header_style_data = workbook.add_format(
            {'font_name': 'Arial', 'font_color': 'black', 'align': 'left'})
        data_style_left = workbook.add_format(
            {'font_name': 'Arial', 'border': True, 'font_color': 'black', 'align': 'left'})
        data_style_center_qty = workbook.add_format(
            {'font_name': 'Arial', 'border': True, 'font_color': 'black', 'align': 'center'})
        data_style_center_total_qty = workbook.add_format(
            {'font_name': 'Arial', 'bold': True, 'font_color': 'black', 'align': 'center'})
        data_style_left_total = workbook.add_format(
            {'font_name': 'Arial', 'bold': True, 'font_color': 'black', 'align': 'left'})
        # End cell style
        worksheet.merge_range(0, 0, 1, 5, "Footwear Non-Footwear Sales Report", header_style_top)
        for key, value in data.items():
            if key == 'other':
                worksheet.merge_range(0, 6, 0, 7, "Start Date:", file_header_style)
                worksheet.merge_range(0, 8, 0, 10, data[key]['date_start'], file_header_style_data)

                worksheet.merge_range(1, 6, 1, 7, "End Date:", file_header_style)
                worksheet.merge_range(1, 8, 1, 10, data[key]['date_stop'], file_header_style_data)

                worksheet.merge_range(2, 6, 2, 7, "Shop Name.:", file_header_style)
                if data[key]['shop_loc']:
                    worksheet.merge_range(2, 8, 2, 10, data[key]['shop_loc'], file_header_style_data)
        row = 3
        col = 0

        worksheet.write(row, col, "Type", header_style)
        worksheet.write(row, col + 1, "Sales Quantity", header_style_sale_qty)
        worksheet.write(row, col + 2, "Amount", header_style_amount)
        total_qty = 0
        total_val = 0
        row = 4
