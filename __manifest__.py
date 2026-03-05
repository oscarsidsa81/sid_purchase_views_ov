# -*- coding: utf-8 -*-
{
    "name": "sid_purchase_views_ov",
    "version": "15.0.1.0.1",
    "category": "Purchases",
    "summary": "Overrides de vistas de Purchase agrupados por funcionalidad.",
    "author": "oscarsidsa81",
    "license": "LGPL-3",
    "depends": [
        "purchase",
        "web",
        "sale_management",
        "sid_purchase_extra_fields",
    ],
    "data": [
        "data/purchase_order_line_actions.xml",
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
            "sid_purchase_views_ov/static/src/scss/sid_list_wrap.scss",
        ],
    },
    "installable": True,
    "application": False,
}
