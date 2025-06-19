"""REST client handling, including MeltanoHubStream base class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterable

import requests
from singer_sdk.streams import Stream

if TYPE_CHECKING:
    from singer_sdk.helpers.types import Context, Record


class MeltanoStream(Stream):
    """MeltanoPlugins stream class."""

    def _get_request(self, url: str) -> dict[str, Any]:
        index_resp = requests.get(
            url,
            headers={"User-Agent": "tap-meltanohub"},
            timeout=10,
        )
        index_resp.raise_for_status()
        return index_resp.json()  # type: ignore[no-any-return]

    def get_records(
        self,
        context: Context | None,
    ) -> Iterable[Record | tuple[dict[str, Any], dict[str, Any] | None]]:
        """Parse the response and return an iterator of result rows."""
        index = self._get_request(self.config["api_url"] + "/meltano/api/v1/plugins/index")
        for plugin_type, plugins_dict in index.items():
            for _, plugin_index_def in plugins_dict.items():
                default_variant = plugin_index_def.get("default_variant")
                for variant_name, variant_detail in plugin_index_def.get("variants").items():
                    plugin = self._get_request(variant_detail.get("ref"))

                    plugin["id"] = f"{plugin_type}--{plugin.get('name')}--{plugin.get('variant')}"
                    plugin["plugin_type"] = plugin_type

                    if variant_name == default_variant:
                        plugin["default"] = True
                    else:
                        plugin["default"] = False

                    yield plugin
