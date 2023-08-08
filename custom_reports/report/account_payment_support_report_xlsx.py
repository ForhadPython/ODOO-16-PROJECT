import base64
import io
from odoo import models


class AccountPaymentTransactionExcelReportsXlsx(models.AbstractModel):
    _name = 'report.custom_reports.payment_support_excel_xlsx'
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

        sheet.merge_range(0, 0, 1, 6, "ACCOUNT PAYMENT SUPPORT", header_style_top)
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
        sheet.merge_range(row, col, row + 1, col, "INVOICE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "INVOICE VALUE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "AMOUNT", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "RETURN VAL", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "CASH", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "CITY VISA", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DBBL VISA", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "UCB VISA", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "BKASH", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DBBL ROCKET", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "CAED VOUCHER", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "OK WALET", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "U PAY", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "GIFT VOUCHER", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "MCS", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "BAY E VOUCHER", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "EMPLOYEE DISCOUNT", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "BEFTN", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "CITY MASTER", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "LANKA BANGLA VISA", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "LANKA BANGLA MASTER", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "I_PAY", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "MTB VISA", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "MTB MASTER", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DBBL NEXUS", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "CITY MAX", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DBBL MASTER", upper_header_style)

        print("@@@@@@@@@@@@@@@@ Test for Action @@@@@@@@@@@@2", data)
