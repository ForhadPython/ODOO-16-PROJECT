import base64
import io
from odoo import models


class RecapShopReportExcelReportsXlsx(models.AbstractModel):
    _name = 'report.custom_reports.recap_shop_report_excel_xlsx'
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

        sheet.merge_range(0, 0, 1, 6, "RECAP SHOP REPORT", header_style_top)
        # for key, value in data.items():
        #     if key == 'other':
        #         sheet.merge_range(1, 1, 7, 7, "Date:", file_header_style)
        #         sheet.merge_range(1, 1, 8, 10, value['date'], file_header_style_data)
        #         sheet.merge_range(2, 2, 7, 7, "Shop Name:", file_header_style)
        #         sheet.merge_range(2, 2, 8, 10, value['shop_name'], file_header_style_data)

        row = 4
        col = 0

        sheet.merge_range(row, col, row + 1, col, "TYPE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DEPARTMENT", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "CAT. CODE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "CATEGORY", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "NO LINE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "YEAR TILL DATE SALE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "THIS PERIOD SALE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "UP TO THIS PERIOD SALE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "OPENING (WITH TRANSIT)", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "PO RECEIVE", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "CDC RECEIVE(SHOP)", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "CDC DISPATCH", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "RECEIVE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DISPATCH", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "SHOP STOCK", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "CDC STOCK", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "DEFECTIVE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "CLAIM", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "ADJUSTMENT", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "CIRCULAR", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "GOODS ON WAY", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "CLOSING (WITH TRANSIT)", upper_header_style)

        print("@@@@@@@@@@@@@@@@ Test for Action @@@@@@@@@@@@2", data)
