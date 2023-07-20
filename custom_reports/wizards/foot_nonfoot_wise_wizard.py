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

    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    shop_loc_id = fields.Char(string="Shop Name")

    def action_generate_excel_report(self, data):
        """ Footwear and non Footwear Excel report object method """
        filename = 'Footwear and Non Footwear Report'
        # workbook = xlsxwriter.Workbook(filename)

        file_data = io.StringIO()

        workbook = xlsxwriter.Workbook(file_data)
        worksheet = workbook.add_worksheet()
        data['other'] = {
            'date_start': self.start_date,
            'date_stop': self.end_date,
            'shop_loc_id': self.stock_loc_id,
        }

        foo_nonfoot_report_ids = self.env['']

        data['ids'] = foo_nonfoot_report_ids.get_foot_nonfoot_sales(data['other']['date_start'],
                                                                    data['other']['date_stop'],
                                                                    data['other']['shop_loc_id'])

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
            'res_model': 'foot.nonfoot.report.wizard',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    # def _excel_plot_for_foot_and_nonfoot_report(data, worksheet, workbook):
    #     """ Method to generate excel report for shop wise stock report """
    #     # Start Cell Styl
    #     header_style_top = workbook.add_format(
    #         {'align': 'center', 'border': True, 'font_name': 'Arial', 'font_color': 'black', 'bold': True,
    #          'font_size': 17})
    #     header_style = workbook.add_format(
    #         {'align': 'center', 'border': True, 'bold': True, 'font_name': 'Arial', 'font_color': 'black',
    #          'font_size': 11})
    #     header_style_sale_qty = workbook.add_format(
    #         {'align': 'center', 'border': True, 'bold': True, 'font_name': 'Arial', 'font_color': 'black',
    #          'font_size': 11})
    #     header_style_amount = workbook.add_format(
    #         {'align': 'center', 'border': True, 'bold': True, 'font_name': 'Arial', 'font_color': 'black',
    #          'font_size': 11})
    #     file_header_style = workbook.add_format(
    #         {'font_name': 'Arial', 'font_color': 'black', 'bold': True})
    #     file_header_style_data = workbook.add_format(
    #         {'font_name': 'Arial', 'font_color': 'black', 'align': 'left'})
    #     data_style_left = workbook.add_format(
    #         {'font_name': 'Arial', 'border': True, 'font_color': 'black', 'align': 'left'})
    #     data_style_center_qty = workbook.add_format(
    #         {'font_name': 'Arial', 'border': True, 'font_color': 'black', 'align': 'center'})
    #     data_style_center_total_qty = workbook.add_format(
    #         {'font_name': 'Arial', 'bold': True, 'font_color': 'black', 'align': 'center'})
    #     data_style_left_total = workbook.add_format(
    #         {'font_name': 'Arial', 'bold': True, 'font_color': 'black', 'align': 'left'})
    #     # End cell style
    #     worksheet.merge_range(0, 0, 1, 5, "Footwear Non-Footwear Sales Report", header_style_top)
    #     for key, value in data.items():
    #         if key == 'other':
    #             worksheet.merge_range(0, 6, 0, 7, "Start Date:", file_header_style)
    #             worksheet.merge_range(0, 8, 0, 10, data[key]['date_start'], file_header_style_data)
    #
    #             worksheet.merge_range(1, 6, 1, 7, "End Date:", file_header_style)
    #             worksheet.merge_range(1, 8, 1, 10, data[key]['date_stop'], file_header_style_data)
    #
    #             worksheet.merge_range(2, 6, 2, 7, "Shop Name.:", file_header_style)
    #             if data[key]['shop_loc']:
    #                 worksheet.merge_range(2, 8, 2, 10, data[key]['shop_loc'], file_header_style_data)
    #     row = 3
    #     col = 0
    #
    #     worksheet.write(row, col, "Type", header_style)
    #     worksheet.write(row, col + 1, "Sales Quantity", header_style_sale_qty)
    #     worksheet.write(row, col + 2, "Amount", header_style_amount)
    #     total_qty = 0
    #     total_val = 0
    #     row = 4




    # start_date = fields.Datetime(string="Start Date",
    #                              default=time.strftime('%Y-%m-01'),
    #                              required=True)
    # end_date = fields.Datetime(string="End Date",
    #                            default=datetime.datetime.now(),
    #                            required=True)

    # def print_xlsx(self):
    #     if self.start_date > self.end_date:
    #         raise ValidationError('Start Date must be less than End Date')
    #     data = {
    #         'start_date': self.start_date,
    #         'end_date': self.end_date,
    #     }
    # return {
    #     'type': 'ir.actions.report',
    #     'data': {'model': 'example.xlsx.wizard',
    #              'options': json.dumps(data,
    #                                    default=date_utils.json_default),
    #              'output_format': 'xlsx',
    #              'report_name': 'Excel Report',
    #              },
    #     'report_type': 'xlsx',
    # }
    #
    # def get_xlsx_report(self, data, response):
    #     from_date = data['from_date']
    #     to_date = data['to_date']
    #     output = io.BytesIO()
    #     workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    #     sheet = workbook.add_worksheet()
    #     cell_format = workbook.add_format(
    #         {'font_size': '12px', 'align': 'center'})
    #
    # head = workbook.add_format(
    #     {'align': 'center', 'bold': True, 'font_size': '20px'})
    # txt = workbook.add_format({'font_size': '10px', 'align': 'center'})
    # sheet.merge_range('B2:I3', EXCEL REPORT', head)
    # sheet.merge_range('A6:B6', 'From Date:', cell_format)
    # sheet.merge_range('C6:D6', from_date, txt)
    # sheet.write('F6', 'To Date:', cell_format)
    # sheet.merge_range('G6:H6', to_date, txt)
    # workbook.close()
    # output.seek(0)
    # response.stream.write(output.read())
    # output.close()
