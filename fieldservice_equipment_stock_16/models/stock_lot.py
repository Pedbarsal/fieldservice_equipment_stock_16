# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

'''
Cambios:
- La clase ahora hereda de ‘stock.lot’ en vez de ‘stock.production.lot’.
- La clase ha pasado a llamarse ‘StockLot’.
- El archivo ha pasado a llamarse ‘stock_lot.py’.
'''

from odoo import fields, models

class StockLot(models.Model):
    _inherit = "stock.lot"

    fsm_equipment_id = fields.Many2one(
        "fsm.equipment", string="Equipment", readonly=True
    )
