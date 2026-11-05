# Part of Bancada. See LICENSE file for full copyright and licensing details.
{
    "name": "Odoo MCP for Claude (Bancada)",
    "version": "17.0.1.0.0",
    "category": "Productivity",
    "summary": "Free helper to connect Claude to Odoo with the Odoo MCP connector (paid external service, free trial).",
    "description": """
Odoo MCP for Claude (Bancada)
=============================

**This module is free. The Odoo MCP service is paid**: it is an external service
run by Bancada, contracted at https://mcp-odoo.bancada.es, with a free trial
(200 free calls, no card required). Plans and prices: https://mcp-odoo.bancada.es/#precios

The module only helps you configure the connector. It adds Settings > Claude (Odoo MCP)
with the connector URL, the three setup steps and a button that opens the standard Odoo
dialog to create an API key. It makes no external calls, has no telemetry and stores nothing.
""",
    "author": "Bancada",
    "website": "https://mcp-odoo.bancada.es",
    "support": "hola@bancada.es",
    "license": "LGPL-3",
    "price": 0.0,
    "currency": "EUR",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/mcp_setup_views.xml",
    ],
    "images": [
        "static/description/banner.png",
        "static/description/screenshot_settings.png",
        "static/description/screenshot_steps.png",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
