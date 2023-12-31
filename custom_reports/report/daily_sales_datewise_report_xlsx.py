import base64
import io
from odoo import models


class DailySalesDatewiseExcelReportsXlsx(models.AbstractModel):
    _name = 'report.custom_reports.daily_sales_datewise_excel_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, worksheet):
        """ Method to generate excel report for mobile data report """
        sheet = workbook.add_worksheet('name')
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

        sheet.merge_range(0, 0, 1, 6, "DAILY SALES DATE WISE REPORT", header_style_top)
        # for key, value in data.items():
        #     if key == 'other':
        #         sheet.merge_range(1, 1, 7, 7, "Date:", file_header_style)
        #         sheet.merge_range(1, 1, 8, 10, value['date'], file_header_style_data)
        #         sheet.merge_range(2, 2, 7, 7, "Shop Name:", file_header_style)
        #         sheet.merge_range(2, 2, 8, 10, value['shop_name'], file_header_style_data)

        row = 4
        col = 0

        sheet.merge_range(row, col, row + 1, col, "SHOP NAME", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "SHOP CODE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DATE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "PAIR SHOE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "PAIR TURNOVER", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "PIECE NON FOOTWEAR", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "NON FOOTWEAR TURNOVER", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "PAIR/PIECE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "TOTAL TURNOVER", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DISCOUNT PAIR SHOE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DISCOUNT PAIR VALUE(after)", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DISCOUNT PIECE NON FOOTWEAR", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DISCOUNT NON FOOTWEAR VALUE(after)", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "PAIR/PIECE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DISCOUNT TOTAL VALUE(after)", upper_header_style)

        print("@@@@@@@@@@@@@@@@ Test for Action @@@@@@@@@@@@2", data)
