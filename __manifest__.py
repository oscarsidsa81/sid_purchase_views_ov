# -*- coding: utf-8 -*-
{
    "name": "SIDSA - Purchase Views",
    "version": "15.0.1.0.0",
    "category": "Purchases",
    "summary": "Overrides de vistas de Purchase agrupados por funcionalidad.",
    "author": "SIDSA / Custom",
    "license": "LGPL-3",
    "depends": [
        "purchase",
        "sale_management",
        "sid_purchase_extra_fields",
    ],
    "data": [
        "views/purchase_order/tree_base.xml",
        "views/purchase_order/form_buttons.xml",
        "views/purchase_order/form_varios.xml",
        "views/purchase_order_line/tree_buttons.xml",
        "views/purchase_order_line/tree_columns.xml",
        "views/purchase_order_line/tree_decorations.xml",
        "views/purchase_order_line/form_contract_date.xml",
        "views/purchase_order_line/search.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "sid_purchase_views/static/src/scss/sid_list_wrap.scss",
        ],
    },
    "installable": True,
    "application": False,
}
