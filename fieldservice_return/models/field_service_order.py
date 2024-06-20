from odoo import models, fields, api

class FieldServiceOrder(models.Model):
    _inherit = 'field.service.order'

    def action_complete(self):
        res = super(FieldServiceOrder, self).action_complete()
        for order in self:
            for move in order.inventory_move_ids:
                return_move = self.env['stock.move'].create({
                    'name': move.name,
                    'product_id': move.product_id.id,
                    'product_uom_qty': move.product_uom_qty,
                    'product_uom': move.product_uom.id,
                    'location_id': move.location_dest_id.id,
                    'location_dest_id': move.location_id.id,
                    'origin': move.origin,
                    'state': 'draft',
                })
                return_move._action_confirm()
                return_move._action_assign()
                return_move._action_done()
        return res

class StockMove(models.Model):
    _inherit = 'stock.move'

    service_order_id = fields.Many2one('field.service.order', string='Service Order')

class FieldServiceOrder(models.Model):
    _inherit = 'field.service.order'

    inventory_move_ids = fields.One2many(
        'stock.move', 'service_order_id', string='Inventory Moves'
    )

class StockMove(models.Model):
    _inherit = 'stock.move'

    service_order_id = fields.Many2one('field.service.order', string='Service Order')
