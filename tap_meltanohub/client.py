"""REST client handling, including MeltanoHubStream base class."""

from pathlib import Path
from typing import Iterable, Optional

import requests
from singer_sdk.streams import RESTStream, Stream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class SingerStream(RESTStream):
    """SingerStream stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"] + "/singer/api/v1"


class MeltanoStream(Stream):
    """MeltanoPlugins stream class."""

    def _get_request(self, url):
        index_resp = requests.get(url)
        index_resp.raise_for_status()
        return index_resp.json()

    def get_records(self, context: Optional[dict]) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        index = self._get_request(
            self.config["api_url"] + "/meltano/api/v1/plugins/index"
        )
        for plugin_type, plugins_dict in index.items():
            for _, plugin_index_def in plugins_dict.items():
                default_variant = plugin_index_def.get("default_variant")
                for variant_name, variant_detail in plugin_index_def.get(
                    "variants"
                ).items():
                    plugin_definition = self._get_request(variant_detail.get("ref"))

                    plugin_definition[
                        "id"
                    ] = f"{plugin_type}--{plugin_definition.get('name')}--{plugin_definition.get('variant')}"
                    plugin_definition["plugin_type"] = plugin_type

                    if variant_name == default_variant:
                        plugin_definition["default"] = True
                    else:
                        plugin_definition["default"] = False

                    yield plugin_definition
