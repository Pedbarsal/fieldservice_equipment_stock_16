#Documentación de cambios

**Módulo:** fieldservice_equipment_stock

**Versión original:** 14.0.1.1.0

**Versión migrada:** 16.0.1.0.0

**Fecha de migración:** 5-4-2024

**Autor:** Pedro Barrera Salvador

**Descripción general:**

Este documento recoge los cambios realizados al migrar el módulo fieldservice_equipment_stock, desarrollado por la comunidad para Odoo 14, a la versión 16 de Odoo.


##Lista de cambios:

**Archivos modificados:**

* fieldservice_equipment_stock/models/stock_lot.py
* fieldservice_equipment_stock/models/__init__.py
* fieldservice_equipment_stock/views/stock_lot.xml

**Cambios específicos:**

1. Modificación de la clase StockLot

Se ha renombrado la clase StockProductionLot, al igual que el archivo que la contiene, pasando a llamarse StockLot y stock_lot.py respectivamente. Además, la clase ahora hereda de '''stock.lot''' en vez de '''stock.production.lot'''.

2. Archivo __init__.py

Se ha renombrado '''stock_equipment_lot''', pasando a llamarse '''stock_lot'''.

3. Archivo stock_lot.xml

Se ha renombrado el archivo '''stock_production_lot.xml''', pasando a llamarse '''stock_lot.xml'''.