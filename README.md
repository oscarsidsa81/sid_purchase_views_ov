# sid_purchase_views_ov

## Propósito

Overrides de vistas (OV) para compras:

- `purchase.order` (form/tree)
- `purchase.order.line` (tree/search/form)

## Dependencias

- `sid_purchase_extra_fields` (meta), que instala `sid_purchase_core` y `sid_purchase_delay_sync`.

## Contenido

Ver carpeta `views/` y `data/`.

## Notas de instalación y validación

### Decoraciones en líneas de pedido de compra

La vista heredada `view_purchase_order_line_tree_decorations_sid` añade decoraciones de fila a `purchase.order.line`:

- `decoration-warning` para líneas pendientes.
- `decoration-danger` para líneas marcadas para facturar.
- `decoration-muted` para líneas canceladas.

Odoo valida que todos los campos usados en expresiones `decoration-*` existan en la vista. Por eso `views/purchase_order_line/tree_decorations.xml` incluye el campo técnico `state` como invisible: es necesario para evaluar `decoration-muted="state == 'cancel'"` y evitar errores de validación al instalar o actualizar el módulo.
