from odoo import api, fields, models


class RootReportsAction(models.Model):
    _name = "reports.action.data"
    _description = "Reports Action Data"

    name = fields.Char(string="Name", size=200, required=True)
    Age = fields.Integer(string="Age", size=128, required=True)
