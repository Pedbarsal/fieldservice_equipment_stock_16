# models/sale_order.py
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            for line in order.order_line:
                if line.product_id.type == 'service' and line.product_id.service_tracking == 'task_global_project':
                    # Encuentra la orden de servicio relacionada
                    service_order = self.env['field.service.order'].search([('sale_order_id', '=', order.id)], limit=1)
                    if service_order:
                        # Crear movimientos de inventario para los equipos necesarios
                        for equipment in service_order.equipment_ids:
                            self.env['stock.move'].create({
                                'name': equipment.product_id.name,
                                'product_id': equipment.product_id.id,
                                'product_uom_qty': equipment.quantity,
                                'product_uom': equipment.product_id.uom_id.id,
                                'location_id': self.env.ref('stock.stock_location_stock').id,
                                'location_dest_id': order.partner_shipping_id.property_stock_customer.id,
                                'sale_line_id': line.id,
                                'state': 'draft',
                            })
        return res
