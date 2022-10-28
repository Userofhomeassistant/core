"""Diagnostics support for Environment Canada."""
from __future__ import annotations

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE
from homeassistant.core import HomeAssistant

from .const import DOMAIN

TO_REDACT = {CONF_LATITUDE, CONF_LONGITUDE}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, config_entry: ConfigEntry
) -> dict:
    """Return diagnostics for a config entry."""
    coordinators = hass.data[DOMAIN][config_entry.entry_id]
    weather_coord = coordinators["weather_coordinator"]

    diagnostics_data = {
        "config_entry_data": async_redact_data(dict(config_entry.data), TO_REDACT),
        "weather_data": dict(weather_coord.ec_data.conditions),
    }

    return diagnostics_data
