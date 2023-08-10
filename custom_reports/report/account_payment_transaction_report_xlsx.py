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
        # worksheet.write(row + 1, col, "PAIR SHOE", header_style)
        # worksheet.write(row + 1, col + 1, "DEPOSIT", header_style)
        # worksheet.write(row + 1, col + 2, "DEPOSIT DATE", header_style)

        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "CITY BANK", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "MTBL", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "UCBL", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "BRAC BANK", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "ROCKET", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "NAGAD", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "BKSH", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "U PAY", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col + 2, "OK WALET", upper_header_style)

        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "E-COMMERCE COMMISSION & DELIVERY CHARGE", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "CASH COLLECTION", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "GIFT VOUCHER", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "MCS", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "BAY E VOUCHAR", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "CARD VOUCHAR", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "EMPLOYEE VOUCHAR", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "BEFTN", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "BANK INSTRUMENTS", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "AGRONI DEPOSIT", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "BILL", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "TOTAL RECEIVED", upper_header_style)
        col = col + 3
        sheet.merge_range(row, col, row + 1, col, "CASH IN SHOP", upper_header_style)
