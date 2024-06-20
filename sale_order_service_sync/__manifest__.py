# __manifest__.py
{
    'name': 'Sale Order Service Sync',
    'version': '1.0',
    'summary': 'Notifica los productos del pedido de ventas al apartado inventario de la orden de servicio de campo',
    'description': 'Modulo personaizado, para la sincronizacion de los productos contenidos en el pedido de ventas y el apartado inventario de la orden de servicio de campo asociadas.',
    'author': 'Pedro Barrera',
    'depends': ['sale', 'stock', 'sale_management', 'fieldservice'],
    'data': [],
    'installable': True,
    'auto_install': False,
}
