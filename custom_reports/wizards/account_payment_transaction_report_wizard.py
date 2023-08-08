import time
import datetime
from urllib import response

from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.tools import float_is_zero
from odoo.tools import date_utils
import io
import json


class AccountPaymentTransactionReportWizard(models.TransientModel):
    """ Account Payment Transaction Report Wizard """
    _name = 'account.payment.transaction.report.wizard'
    _description = "Account Payment Transaction Report"

    excel_file = fields.Binary('Excel Report')
    file_name = fields.Char('Excel File', size=64)

    @api.model
    def _get_current_date(self):
        """ :return current date """
        return fields.Date.today()

    date = fields.Date(string="Date", required=True, default=lambda self: self._get_current_date())
    location_id = fields.Char(string="Shop")

    def generate_account_payment_transaction_excel_report(self):
        print("EXCEL REPORT TESTING")
        data = {}
        return self.env.ref('custom_reports.payment_transaction_excel_xlsx').report_action(self, data=data)

# def _excel_account_payment_transaction_report(data, worksheet):
#     header_style_left = xlwt.easyxf(
#         'font: color-index black, bold on, height 180; align: horiz left; borders: top_color black, '
#         'bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;')
#
#     header_style_left_g1 = xlwt.easyxf(
#         'font: color-index black,bold on, height 180; pattern: back_colour black; align: horiz left; borders: '
#         'top_color black, '
#         'bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;')
#
#     random_number_center = xlwt.easyxf(
#         'font: color-index black, height 180; pattern: back_colour black; align: horiz center; borders: '
#         'top_color black,'
#         'bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;')
#
#     random_number_center_sl = xlwt.easyxf(
#         'font: color-index black,bold on, height 180; pattern: back_colour black; align: horiz center; borders: '
#         'top_color black,'
#         'bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;')
#
#     header_style = xlwt.easyxf(
#         'font: color-index black, bold on, height 180; align: horiz center; borders: top_color black, bottom_color '
#         'black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;')
#
#     upper_header_style = xlwt.easyxf(
#         'font: color-index black, bold on, height 200; align: horiz center; borders: top_color black, bottom_color '
#         'black ,right_color black, left_color black, left thin, right thin, top thin, bottom thin;')
#
#     file_name_style = xlwt.easyxf('font: color-index green, bold on, height 400;align: horiz center')
#     file_header_style = xlwt.easyxf('font: color-index black, bold on, height 210')
#     file_header_style_data = xlwt.easyxf('font: color-index black, height 210')
#     data_style_left = xlwt.easyxf("align: horiz left")
#
#     worksheet.write_merge(1, 2, 1, 6, "ACCOUNT PAYMENT TRANSACTION", file_name_style)
#     for key, value in data.items():
#         if key == 'other':
#             worksheet.write_merge(1, 1, 7, 7, "Date:", file_header_style)
#             worksheet.write_merge(1, 1, 8, 10, value['date'], file_header_style_data)
#             worksheet.write_merge(2, 2, 7, 7, "Shop Name:", file_header_style)
#             worksheet.write_merge(2, 2, 8, 10, value['shop_name'], file_header_style_data)
#
#     row = 4
#     col = 0
#
#     worksheet.write_merge(row, row + 1, col, col, "SL", random_number_center_sl)
#     worksheet.write_merge(row, row + 1, col + 1, col + 1, "SHOP NAME", header_style_left_g1)
#     worksheet.write_merge(row, row + 1, col + 2, col + 2, "SHOP CODE", header_style_left_g1)
#     worksheet.write_merge(row, row + 1, col + 3, col + 3, "TERRITORY CODE", header_style_left_g1)
#     worksheet.write_merge(row, row + 1, col + 4, col + 4, "SHOP MOBILE NO", header_style_left_g1)
#     worksheet.write_merge(row, row + 1, col + 5, col + 5, "OPENING BALANCE", header_style_left_g1)
#     worksheet.write_merge(row, row + 1, col + 6, col + 6, "DAY SALES", header_style_left_g1)
#     worksheet.write_merge(row, row + 1, col + 7, col + 7, "TOTAL", header_style_left)
#
#     worksheet.write_merge(row, row, col + 8, col + 10, "DUTCH BANGLA BANK", upper_header_style)
#     worksheet.write_merge(row, row, col + 11, col + 13, " CITY BANK", upper_header_style)
#     worksheet.write_merge(row, row, col + 14, col + 16, "MTBL", upper_header_style)
#     worksheet.write_merge(row, row, col + 17, col + 19, "UCBL", upper_header_style)
#     worksheet.write_merge(row, row, col + 20, col + 22, "BRAC BANK", upper_header_style)
#
#     worksheet.write_merge(row, row, col + 23, col + 25, "ROCKET", upper_header_style)
#     worksheet.write_merge(row, row, col + 26, col + 28, "NAGAD", upper_header_style)
#     worksheet.write_merge(row, row, col + 29, col + 31, "BKSH", upper_header_style)
#     worksheet.write_merge(row, row, col + 32, col + 34, "U PAY", upper_header_style)
#     worksheet.write_merge(row, row, col + 35, col + 37, "OK WALET", upper_header_style)
#
#     worksheet.write(row + 1, col + 8, "CARD", header_style)
#     worksheet.write(row + 1, col + 9, "DEPOSIT", header_style)
#     worksheet.write(row + 1, col + 10, "DEPOSIT DATE", header_style)
#
#     worksheet.write(row + 1, col + 11, "CARD", header_style)
#     worksheet.write(row + 1, col + 12, "DEPOSIT", header_style)
#     worksheet.write(row + 1, col + 13, "DEPOSIT DATE", header_style)
#
#     worksheet.write(row + 1, col + 14, "CARD", header_style)
#     worksheet.write(row + 1, col + 15, "DEPOSIT", header_style)
#     worksheet.write(row + 1, col + 16, "DEPOSIT DATE", header_style)
#
#     worksheet.write(row + 1, col + 17, "CARD", header_style)
#     worksheet.write(row + 1, col + 18, "DEPOSIT", header_style)
#     worksheet.write(row + 1, col + 19, "DEPOSIT DATE", header_style)
#
#     worksheet.write(row + 1, col + 20, "CARD", header_style)
#     worksheet.write(row + 1, col + 21, "DEPOSIT", header_style)
#     worksheet.write(row + 1, col + 22, "DEPOSIT DATE", header_style)
#
#     worksheet.write(row + 1, col + 23, "CARD", header_style)
#     worksheet.write(row + 1, col + 24, "DEPOSIT", header_style)
#     worksheet.write(row + 1, col + 25, "DEPOSIT DATE", header_style)
#
#     worksheet.write(row + 1, col + 26, "CARD", header_style)
#     worksheet.write(row + 1, col + 27, "DEPOSIT", header_style)
#     worksheet.write(row + 1, col + 28, "DEPOSIT DATE", header_style)
#
#     worksheet.write(row + 1, col + 29, "CARD", header_style)
#     worksheet.write(row + 1, col + 30, "DEPOSIT", header_style)
#     worksheet.write(row + 1, col + 31, "DEPOSIT DATE", header_style)
#
#     worksheet.write(row + 1, col + 32, "CARD", header_style)
#     worksheet.write(row + 1, col + 33, "DEPOSIT", header_style)
#     worksheet.write(row + 1, col + 34, "DEPOSIT DATE", header_style)
#
#     worksheet.write(row + 1, col + 35, "CARD", header_style)
#     worksheet.write(row + 1, col + 36, "DEPOSIT", header_style)
#     worksheet.write(row + 1, col + 37, "DEPOSIT DATE", header_style)
#
#     worksheet.write_merge(row, row + 1, col + 38, col + 38, "E-COMMERCE COMMISSION & DELIVERY CHARGE",
#                           header_style_left_g1)
#     worksheet.write_merge(row, row + 1, col + 39, col + 39, "CASH COLLECTION", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 40, col + 40, "LANKABANGLA", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 41, col + 41, "GIFT VOUCHER", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 42, col + 42, "MCS", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 43, col + 43, "BAY E VOUCHAR", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 44, col + 44, "CARD VOUCHAR", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 45, col + 45, "EMPLOYEE VOUCHAR", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 46, col + 46, "BEFTN", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 47, col + 47, "BANK INSTRUMENTS", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 48, col + 48, "AGRONI DEPOSIT", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 49, col + 49, "I-PAY", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 50, col + 50, "BILL", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 51, col + 51, "TOTAL RECEIVED", header_style_left)
#     worksheet.write_merge(row, row + 1, col + 52, col + 52, "CASH IN SHOP", header_style_left)
#
#     row = 6
#
#     depo_values = data.get('amount')
#     cash_values = data.get('cash_amount')
#     deposit_values = data.get('deposit_amount')
#
#     shops_deposit_maps = {}
#
#     banks_cols_map = {
#         'DBBL CD': 9,
#         'City CD': 12,
#         'MTB': 15,
#         'UCB': 18,
#         'Brac Bank OD': 21,
#         'ROCKET': 24,
#         'NAGAD': 27,
#         'Cash HO': 29,
#         'Brac bKash': 30,
#         'UPAY': 33,
#         'OK WALET': 36,
#         'Agrani CD': 38
#     }
#
#     grand_totals = {
#         'open_row_deposite': 0,
#         'total_day_sale': 0,
#         'total_val': 0,
#         'dbbl_bank_sum': 0,
#         'city_bank_sum': 0,
#         'mtb_bank_sum': 0,
#         'ucb_bank_sum': 0,
#         'rocket_card_var_data': 0,
#         'nagad_card_var_data': 0,
#         'bksh_card_var_data': 0,
#         'upay_card_var_data': 0,
#         'okwalet_card_var_data': 0,
#         'lanka_bank_sum': 0,
#         'gift_voucher_card_sum': 0,
#         'mcs_card_var_sum': 0,
#         'bay_e_voucher_sum': 0,
#         'card_voucher_var_sum': 0,
#         'employee_voucher_var_sum': 0,
#         'beftn_bank_val_sum': 0,
#         'instrument_bank_var_sum': 0,
#         'ipay_bank_val_sum': 0,
#         'total_deposit_card_payment': 0,
#         'total_val_cash_shop': 0
#     }
#
#     def write_bank_deposit(r=None, c=None, bank=None, deposit=None, d_date=None):
#         # print(r, c, bank, deposit, d_date)
#
#         worksheet.write(r, c + banks_cols_map[bank], deposit, data_style_left)
#         worksheet.write(r, c + banks_cols_map[bank] + 1, d_date, data_style_left)
#
#     total_deposit_cards = {}
#     total_deposits = {}
#     shop_cashes = {}
#
#     for ind, single_record in enumerate(data['ids']):
#         col = 0
#
#         if single_record['bank']:
#
#             key = single_record['shop_code'] + \
#                   str(banks_cols_map[single_record['bank']])
#
#             if key in shops_deposit_maps:
#                 new_date = shops_deposit_maps[key]['date'] + ', ' + single_record['deposit_date']
#
#                 shops_deposit_maps[key]['amount'] += single_record['deposit_amount']
#                 shops_deposit_maps[key]['date'] = new_date
#
#                 write_bank_deposit(
#                     shops_deposit_maps[key]['row'], col,
#                     single_record['bank'], shops_deposit_maps[key]['amount'], new_date)
#
#                 total_received = total_deposit_cards[single_record['shop_code']] + single_record['deposit_amount']
#                 total_deposit = total_deposits[single_record['shop_code']] + single_record['deposit_amount']
#
#                 worksheet.write(shops_deposit_maps[key]['row'], col + 51, total_received, data_style_left)
#
#                 cash_in_shop_val = total_deposit - float(shop_cashes[single_record['shop_code']] or 0)
#                 worksheet.write(shops_deposit_maps[key]['row'], col + 52, round(cash_in_shop_val) or 0, data_style_left)
#                 shop_cashes[single_record['shop_code']] = cash_in_shop_val
#
#                 total_deposit_cards[single_record['shop_code']] = total_received
#                 total_deposits[single_record['shop_code']] = total_deposit
#                 grand_totals['total_deposit_card_payment'] += single_record['deposit_amount']
#
#                 grand_totals[single_record['bank']] = grand_totals.get(
#                     single_record['bank'], 0) + single_record['deposit_amount']
#
#                 continue
#
#             else:
#                 shops_deposit_maps[key] = {
#                     'amount': single_record['deposit_amount'],
#                     'date': single_record['deposit_date'],
#                     'row': row
#                 }
#
#                 write_bank_deposit(
#                     row, col, single_record['bank'],
#                     single_record['deposit_amount'],
#                     single_record['deposit_date'])
#
#                 total_row_deposite = single_record['deposit_amount']
#
#                 grand_totals[single_record['bank']] = grand_totals.get(
#                     single_record['bank'], 0) + total_row_deposite
#
#         else:
#             total_row_deposite = 0.0
#
#         worksheet.write(row, col, ind, random_number_center)
#         worksheet.write(row, col + 1, str(single_record['location_id']).upper(), data_style_left)
#         worksheet.write(row, col + 2, single_record['shop_code'], data_style_left)
#         worksheet.write(row, col + 3, single_record['territory_code'], data_style_left)
#         worksheet.write(row, col + 4, single_record['contact_number'], data_style_left)
#
#         total_day_sale = float(single_record['amount'] or 0)
#         worksheet.write(row, col + 6, total_day_sale, data_style_left)
#         grand_totals['total_day_sale'] += total_day_sale
#
#         dbbl_bank_sum = float(single_record['size_2'] or 0) + float(single_record['size_24'] or 0) + float(
#             single_record['size_26'] or 0)
#         worksheet.write(row, col + 8, dbbl_bank_sum, data_style_left)
#         grand_totals['dbbl_bank_sum'] += dbbl_bank_sum
#
#         city_bank_sum = float(single_record['size_3'] or 0) + float(single_record['size_25'] or 0) + float(
#             single_record['size_18'] or 0)
#         worksheet.write(row, col + 11, city_bank_sum, data_style_left)
#         grand_totals['city_bank_sum'] += city_bank_sum
#
#         mtb_bank_sum = float(single_record['size_5'] or 0) + float(single_record['size_23'] or 0)
#         worksheet.write(row, col + 14, mtb_bank_sum, data_style_left)
#         grand_totals['mtb_bank_sum'] += mtb_bank_sum
#
#         ucb_bank_sum = float(single_record['size_4'] or 0) + float(single_record['size_21'] or 0)
#         worksheet.write(row, col + 17, ucb_bank_sum, data_style_left)
#         grand_totals['ucb_bank_sum'] += ucb_bank_sum
#
#         rocket_card_var_data = float(single_record['size_7'] or 0)
#         worksheet.write(row, col + 23, rocket_card_var_data, data_style_left)
#         grand_totals['rocket_card_var_data'] += rocket_card_var_data
#
#         nagad_card_var_data = float(single_record['size_8'] or 0)
#         worksheet.write(row, col + 26, nagad_card_var_data, data_style_left)
#         grand_totals['nagad_card_var_data'] += nagad_card_var_data
#
#         bksh_card_var_data = float(single_record['size_6'] or 0)
#         worksheet.write(row, col + 29, bksh_card_var_data, data_style_left)
#         grand_totals['bksh_card_var_data'] += bksh_card_var_data
#
#         upay_card_var_data = float(single_record['size_10'] or 0)
#         worksheet.write(row, col + 32, upay_card_var_data, data_style_left)
#         grand_totals['upay_card_var_data'] += upay_card_var_data
#
#         okwalet_card_var_data = float(single_record['size_9'] or 0)
#         worksheet.write(row, col + 35, okwalet_card_var_data, data_style_left)
#         grand_totals['okwalet_card_var_data'] += okwalet_card_var_data
#
#         lanka_bank_sum = float(single_record['size_19'] or 0) + float(single_record['size_20'] or 0)
#         worksheet.write(row, col + 40, lanka_bank_sum, data_style_left)
#         grand_totals['lanka_bank_sum'] += lanka_bank_sum
#
#         gift_voucher_card_sum = float(single_record['size_11'] or 0)
#         worksheet.write(row, col + 41, gift_voucher_card_sum, data_style_left)
#         grand_totals['gift_voucher_card_sum'] += gift_voucher_card_sum
#
#         mcs_card_var_sum = float(single_record['size_12'] or 0)
#         worksheet.write(row, col + 42, mcs_card_var_sum, data_style_left)
#         grand_totals['mcs_card_var_sum'] += mcs_card_var_sum
#
#         bay_e_voucher_sum = float(single_record['size_13'] or 0)
#         worksheet.write(row, col + 43, bay_e_voucher_sum, data_style_left)
#         grand_totals['bay_e_voucher_sum'] += bay_e_voucher_sum
#
#         card_voucher_var_sum = float(single_record['size_14'] or 0)
#         worksheet.write(row, col + 44, card_voucher_var_sum, data_style_left)
#         grand_totals['card_voucher_var_sum'] += card_voucher_var_sum
#
#         employee_voucher_var_sum = float(single_record['size_15'] or 0)
#         worksheet.write(row, col + 45, employee_voucher_var_sum, data_style_left)
#         grand_totals['employee_voucher_var_sum'] += employee_voucher_var_sum
#
#         beftn_bank_val_sum = float(single_record['size_16'] or 0)
#         worksheet.write(row, col + 46, beftn_bank_val_sum, data_style_left)
#         grand_totals['beftn_bank_val_sum'] += beftn_bank_val_sum
#
#         instrument_bank_var_sum = float(single_record['size_17'] or 0)
#         worksheet.write(row, col + 47, instrument_bank_var_sum, data_style_left)
#         grand_totals['instrument_bank_var_sum'] += instrument_bank_var_sum
#
#         ipay_bank_val_sum = float(single_record['size_22'] or 0)
#         worksheet.write(row, col + 49, ipay_bank_val_sum, data_style_left)
#         grand_totals['ipay_bank_val_sum'] += ipay_bank_val_sum
#
#         if row == 9:
#             a = 1
#
#         total_deposit_card_payment = round(float(single_record['size_2'] or 0) + float(
#             single_record['size_3'] or 0) + float(single_record['size_4'] or 0) + float(
#             single_record['size_5'] or 0) + float(single_record['size_6'] or 0) + float(
#             single_record['size_7'] or 0) + float(single_record['size_8'] or 0) + float(
#             single_record['size_9'] or 0) + float(single_record['size_10'] or 0) + float(
#             single_record['size_11'] or 0) + float(single_record['size_12'] or 0) + float(
#             single_record['size_13'] or 0) + float(single_record['size_14'] or 0) + float(
#             single_record['size_15'] or 0) + float(single_record['size_16'] or 0) + float(
#             single_record['size_17'] or 0) + float(single_record['size_18'] or 0) + float(
#             single_record['size_19'] or 0) + float(single_record['size_20'] or 0) + float(
#             single_record['size_21'] or 0) + float(single_record['size_22'] or 0) + float(
#             single_record['size_23'] or 0) + float(single_record['size_24'] or 0) + float(
#             single_record['size_25'] or 0) + float(single_record['size_26'] or 0) + float(
#             total_row_deposite or 0), 2)
#
#         worksheet.write(row, col + 51, total_deposit_card_payment, data_style_left)
#         grand_totals['total_deposit_card_payment'] += total_deposit_card_payment
#
#         total_deposit_cards[single_record['shop_code']] = total_deposit_card_payment
#         total_deposits[single_record['shop_code']] = total_row_deposite
#
#         cash_filtered_list = list(
#             filter(lambda shop: shop['name'] == single_record['location_id'], cash_values))
#         row_cash = 0.0
#         for caval in cash_filtered_list:
#             if caval['p_method'] == 'Cash':
#                 total_cash = float(caval['cash_amount'] or 0)
#                 row_cash = total_cash
#
#         depo_filtered_list = list(
#             filter(lambda shop: shop['shop_id'] == single_record['location_id'], depo_values))
#         row_depo = 0.0
#         for dval in depo_filtered_list:
#             row_depo = float(dval['amount'] or 0)
#
#         # Opening Balance
#         row_shop_val = round(float(row_depo or 0) - float(row_cash or 0))
#         worksheet.write(row, col + 5, row_shop_val, data_style_left)
#         grand_totals['open_row_deposite'] += row_shop_val
#
#         # Total Balance
#         total_val = float(single_record['amount'] or 0) - float(row_shop_val)
#         worksheet.write(row, col + 7, total_val, data_style_left)
#         grand_totals['total_val'] += total_val
#
#         cash_in_shop_val = round(float(total_row_deposite or 0) - float(single_record['size_1'] or 0))
#         worksheet.write(row, col + 52, cash_in_shop_val, data_style_left)
#         grand_totals['total_val_cash_shop'] += cash_in_shop_val
#
#         shop_cashes[single_record['shop_code']] = cash_in_shop_val
#
#         row += 1
#
#     # print(shop_cashes)
#
#     # Total Value in sheet
#     col = 0
#     worksheet.write(row, col + 1, "GRAND TOTAL:", random_number_center_sl)
#     worksheet.write(row, col + 5, grand_totals['open_row_deposite'], random_number_center_sl)
#     worksheet.write(row, col + 6, grand_totals['total_day_sale'], random_number_center_sl)
#     worksheet.write(row, col + 7, grand_totals['total_val'], random_number_center_sl)
#     worksheet.write(row, col + 8, grand_totals['dbbl_bank_sum'], random_number_center_sl)
#     worksheet.write(row, col + 9, grand_totals.get('DBBL CD', 0), random_number_center_sl)
#     worksheet.write(row, col + 11, grand_totals['city_bank_sum'], random_number_center_sl)
#     worksheet.write(row, col + 12, grand_totals.get('City CD', 0), random_number_center_sl)
#     worksheet.write(row, col + 14, grand_totals['mtb_bank_sum'], random_number_center_sl)
#     worksheet.write(row, col + 15, grand_totals.get('MTB', 0), random_number_center_sl)
#     worksheet.write(row, col + 17, grand_totals['ucb_bank_sum'], random_number_center_sl)
#     worksheet.write(row, col + 18, grand_totals.get('UCB', 0), random_number_center_sl)
#     worksheet.write(row, col + 21, grand_totals.get('Brac Bank OD', 0), random_number_center_sl)
#     worksheet.write(row, col + 23, grand_totals['rocket_card_var_data'], random_number_center_sl)
#     worksheet.write(row, col + 24, grand_totals.get('ROCKET', 0), random_number_center_sl)
#     worksheet.write(row, col + 26, grand_totals['nagad_card_var_data'], random_number_center_sl)
#     worksheet.write(row, col + 27, grand_totals.get('NAGAD', 0), random_number_center_sl)
#     worksheet.write(row, col + 29, grand_totals['bksh_card_var_data'], random_number_center_sl)
#     worksheet.write(row, col + 30, grand_totals.get('Brac bKash', 0), random_number_center_sl)
#     worksheet.write(row, col + 32, grand_totals['upay_card_var_data'], random_number_center_sl)
#     worksheet.write(row, col + 33, grand_totals.get('UPAY', 0), random_number_center_sl)
#     worksheet.write(row, col + 35, grand_totals['okwalet_card_var_data'], random_number_center_sl)
#     worksheet.write(row, col + 36, grand_totals.get('OK WALET', 0), random_number_center_sl)
#     worksheet.write(row, col + 38, grand_totals.get('Agrani CD', 0), random_number_center_sl)
#     worksheet.write(row, col + 40, grand_totals['lanka_bank_sum'], random_number_center_sl)
#     worksheet.write(row, col + 41, grand_totals['gift_voucher_card_sum'], random_number_center_sl)
#     worksheet.write(row, col + 42, grand_totals['mcs_card_var_sum'], random_number_center_sl)
#     worksheet.write(row, col + 43, grand_totals['bay_e_voucher_sum'], random_number_center_sl)
#     worksheet.write(row, col + 44, grand_totals['card_voucher_var_sum'], random_number_center_sl)
#     worksheet.write(row, col + 45, grand_totals['employee_voucher_var_sum'], random_number_center_sl)
#     worksheet.write(row, col + 46, grand_totals['beftn_bank_val_sum'], random_number_center_sl)
#     worksheet.write(row, col + 47, grand_totals['instrument_bank_var_sum'], random_number_center_sl)
#     worksheet.write(row, col + 49, grand_totals['ipay_bank_val_sum'], random_number_center_sl)
#     worksheet.write(row, col + 51, grand_totals['total_deposit_card_payment'], random_number_center_sl)
#     worksheet.write(row, col + 52, sum([float(i or 0) for i in shop_cashes.values()]), random_number_center_sl)
