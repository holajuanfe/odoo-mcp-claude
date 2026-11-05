# Part of Bancada. See LICENSE file for full copyright and licensing details.
from odoo import _, api, fields, models

CONNECTOR_URL = "https://mcp-odoo.bancada.es/mcp"


class BancadaMcpSetup(models.TransientModel):
    """Read-only helper screen. It stores nothing and calls no external service."""

    _name = "bancada.mcp.setup"
    _description = "Claude (Odoo MCP) setup helper"

    name = fields.Char(default="Claude (Odoo MCP)", readonly=True)
    connector_url = fields.Char(string="Connector URL", readonly=True, default=CONNECTOR_URL)
    odoo_url = fields.Char(string="Odoo URL", compute="_compute_connection_data")
    database = fields.Char(string="Database", compute="_compute_connection_data")
    login = fields.Char(string="Login", compute="_compute_connection_data")

    @api.depends_context("uid")
    def _compute_connection_data(self):
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url") or ""
        for rec in self:
            rec.odoo_url = base_url
            rec.database = self.env.cr.dbname
            rec.login = self.env.user.login

    @api.model
    def action_open(self):
        """Open the setup screen (called from the Settings menu)."""
        record = self.create({})
        return {
            "type": "ir.actions.act_window",
            "name": _("Claude (Odoo MCP)"),
            "res_model": self._name,
            "res_id": record.id,
            "view_mode": "form",
            "target": "current",
        }

    def action_create_api_key(self):
        """Open the standard Odoo wizard to create an API key.

        This is the same wizard as Preferences > Account Security > New API Key.
        The module never generates, reads or stores keys.
        """
        return self.env.user.api_key_wizard()
