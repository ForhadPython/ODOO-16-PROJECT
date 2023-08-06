import base64
import io
from odoo import models


class AllCurrentStockExcelReportsXlsx(models.AbstractModel):
    _name = 'report.custom_reports.report_all_current_stock_excel_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, worksheet):
        """ Method to generate excel report for all current stock report """
        worksheet = workbook.add_worksheet('name')
        header_style_top = workbook.add_format(
            {'align': 'center', 'border': True, 'font_name': 'Arial', 'font_color': 'black', 'bold': True,
             'font_size': 18})
        upper_header_style = workbook.add_format(
            {'align': 'center', 'border': True, 'font_name': 'Arial', 'font_color': 'black', 'bold': True,
             'font_size': 11})

        data_style_right = workbook.add_format({'font_name': 'Arial', 'font_color': 'black', 'align': 'right'})
        data_style_left = workbook.add_format({'font_name': 'Arial', 'font_color': 'black', 'align': 'left'})

        worksheet.merge_range(0, 0, 1, 7, "All CURRENT STOCK BARCODE REPORT", header_style_top)

        row = 3
        col = 0
        worksheet.merge_range(row, col, row + 1, col, "SHOP", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "TYPE", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "ARTICLE CODE", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "CATEGORY", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "SUBCATEGORY", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "COMMON BARCODE", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "UNIQ BARCODE", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "PLAN NUMBER", upper_header_style)
        col = col + 1
        worksheet.merge_range(row, col, row + 1, col, "QTY", upper_header_style)


        # for key, value in data.items():
        #     if key == 'other':
        #         worksheet.merge_range(0, 6, 0, 7, "FROM DATE:", file_header_style)
        #         worksheet.merge_range(0, 8, 0, 10, data[key]['data_from'], file_header_style_data)
        #         worksheet.merge_range(1, 6, 1, 7, "TO DATE:", file_header_style)
        #         worksheet.merge_range(1, 8, 1, 10, data[key]['data_to'], file_header_style_data)
        #
        # row = 3
        # col = 0
        # # Column Header
        # sheet.merge_range(row, col, row + 1, col, "SHOP CODE", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "INVOICE", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "MOBILE NO", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "MOBILE STATUS", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "ARTICLE CODE", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "PRODUCT CAT NAME", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "BRAND", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "SALE VALUE", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "DATE", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "TIME", upper_header_style)
        # col = col + 1
        # sheet.merge_range(row, col, row + 1, col, "MONTH", upper_header_style)

        print("@@@@@@@@@@@@@@@@ Test for Action @@@@@@@@@@@@2", data)
