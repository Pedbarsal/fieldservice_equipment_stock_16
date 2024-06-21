El presente repositorio contiene los módulos siguientes:
- **fieldservice_equipment_stock_16**: Módulo desarrollado por la comunidad para la versión 14 de Odoo, migrada a la versión 16.
- **fieldservice_return**: Módulo personalizado para la devolución de los productos contenidos en un pedido de ventas al completar la orden de servicio de campo asociada.
- **sale_order_service_sync**: Módulo personalizado para la notificación de los productos contenidos en el pedido de ventas al apartado inventario de la orden de servicio de campo asociada.

También se ha modificado el código del archivo fsm_order.py del módulo principal fieldservice, además de añadir el campo x_is_assigned, con el fin de impedir que pueda ser seleccionado un equipo que ha sido previamente asignado a otra orden de servicio de campo que está en desarrollo.
