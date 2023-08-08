import base64
import io
from odoo import models


class AccountPaymentTransactionExcelReportsXlsx(models.AbstractModel):
    _name = 'report.custom_reports.payment_transaction_excel_xlsx'
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

        sheet.merge_range(0, 0, 1, 6, "ACCOUNT PAYMENT TRANSACTION", header_style_top)
        # for key, value in data.items():
        #     if key == 'other':
        #         sheet.merge_range(1, 1, 7, 7, "Date:", file_header_style)
        #         sheet.merge_range(1, 1, 8, 10, value['date'], file_header_style_data)
        #         sheet.merge_range(2, 2, 7, 7, "Shop Name:", file_header_style)
        #         sheet.merge_range(2, 2, 8, 10, value['shop_name'], file_header_style_data)

        row = 4
        col = 0

        sheet.merge_range(row, col, row + 1, col, "SL", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "SHOP NAME", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "SHOP CODE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "TERRITORY CODE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "SHOP MOBILE NO", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "OPENING BALANCE", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "DAY SALES", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col, "TOTAL", upper_header_style)
        col = col + 1
        sheet.merge_range(row, col, row + 1, col + 2, "DUTCH BANGLA BANK", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "CITY BANK", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "MTBL", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "UCBL", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "BRAC BANK", upper_header_style)
        #
        # sheet.merge_range(row, row, col + 23, col + 25, "ROCKET", upper_header_style)
        # sheet.merge_range(row, row, col + 26, col + 28, "NAGAD", upper_header_style)
        # sheet.merge_range(row, row, col + 29, col + 31, "BKSH", upper_header_style)
        # sheet.merge_range(row, row, col + 32, col + 34, "U PAY", upper_header_style)
        # sheet.merge_range(row, row, col + 35, col + 37, "OK WALET", upper_header_style)
        #
        # sheet.write(row + 1, col + 8, "CARD", header_style)
        # sheet.write(row + 1, col + 9, "DEPOSIT", header_style)
        # sheet.write(row + 1, col + 10, "DEPOSIT DATE", header_style)
        # col = col + 12
        # sheet.write(row, col, row, col, "CARD", header_style)
        # sheet.write(row + 1, col + 12, "DEPOSIT", header_style)
        # sheet.write(row + 1, col + 13, "DEPOSIT DATE", header_style)
        #
        # sheet.write(row + 1, col + 14, "CARD", header_style)
        # sheet.write(row + 1, col + 15, "DEPOSIT", header_style)
        # sheet.write(row + 1, col + 16, "DEPOSIT DATE", header_style)
        #
        # sheet.write(row + 1, col + 17, "CARD", header_style)
        # sheet.write(row + 1, col + 18, "DEPOSIT", header_style)
        # sheet.write(row + 1, col + 19, "DEPOSIT DATE", header_style)
        #
        # sheet.write(row + 1, col + 20, "CARD", header_style)
        # sheet.write(row + 1, col + 21, "DEPOSIT", header_style)
        # sheet.write(row + 1, col + 22, "DEPOSIT DATE", header_style)
        #
        # sheet.write(row + 1, col + 23, "CARD", header_style)
        # sheet.write(row + 1, col + 24, "DEPOSIT", header_style)
        # sheet.write(row + 1, col + 25, "DEPOSIT DATE", header_style)
        #
        # sheet.write(row + 1, col + 26, "CARD", header_style)
        # sheet.write(row + 1, col + 27, "DEPOSIT", header_style)
        # sheet.write(row + 1, col + 28, "DEPOSIT DATE", header_style)
        #
        # sheet.write(row + 1, col + 29, "CARD", header_style)
        # sheet.write(row + 1, col + 30, "DEPOSIT", header_style)
        # sheet.write(row + 1, col + 31, "DEPOSIT DATE", header_style)
        #
        # sheet.write(row + 1, col + 32, "CARD", header_style)
        # sheet.write(row + 1, col + 33, "DEPOSIT", header_style)
        # sheet.write(row + 1, col + 34, "DEPOSIT DATE", header_style)
        #
        # sheet.write(row + 1, col + 35, "CARD", header_style)
        # sheet.write(row + 1, col + 36, "DEPOSIT", header_style)
        # sheet.write(row + 1, col + 37, "DEPOSIT DATE", header_style)
        #
        # sheet.merge_range(row, row + 1, col + 38, col + 38, "E-COMMERCE COMMISSION & DELIVERY CHARGE",
        #                       upper_header_style)
        # sheet.merge_range(row, row + 1, col + 39, col + 39, "CASH COLLECTION", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 40, col + 40, "LANKABANGLA", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 41, col + 41, "GIFT VOUCHER", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 42, col + 42, "MCS", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 43, col + 43, "BAY E VOUCHAR", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 44, col + 44, "CARD VOUCHAR", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 45, col + 45, "EMPLOYEE VOUCHAR", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 46, col + 46, "BEFTN", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 47, col + 47, "BANK INSTRUMENTS", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 48, col + 48, "AGRONI DEPOSIT", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 49, col + 49, "I-PAY", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 50, col + 50, "BILL", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 51, col + 51, "TOTAL RECEIVED", upper_header_style)
        # sheet.merge_range(row, row + 1, col + 52, col + 52, "CASH IN SHOP", upper_header_style)

        print("@@@@@@@@@@@@@@@@ Test for Action @@@@@@@@@@@@2", data)
