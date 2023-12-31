{
    'name': 'Bay Reports',
    'version': '1.0.0',
    'website': 'https://www.amarbay.com',
    'category': 'Bay Reports',
    'sequence': -100,
    'summary': 'Bay customs Reports',
    'depends': ['report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'wizards/foot_nonfoot_wise_wizard_views.xml',
        'wizards/inventory_stock_report_wizard_views.xml',
        'wizards/for_test_print_excel_report_wizard_view.xml',
        'wizards/mobile_data_wizard_views.xml',
        'wizards/send_received_report_wizard_views.xml',
        'wizards/inventory_stock_report_datewise_wizard_views.xml',
        'wizards/all_current_stock_barcode_wizard_views.xml',
        'wizards/point_report_wizard_views.xml',
        'wizards/account_payment_transaction_report_wizard_views.xml',
        'wizards/account_payment_support_report_wizard_views.xml',
        'wizards/daily_sales_datewise_wizard_views.xml',
        'wizards/recap_shop_report_wizard_views.xml',
        'report/report.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
