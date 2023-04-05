"""MeltanoHub tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_meltanohub.streams import MeltanoPlugins

STREAM_TYPES = [MeltanoPlugins]


class TapMeltanoHub(Tap):
    """MeltanoHub tap class."""

    name = "tap-meltanohub"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_url",
            th.StringType,
            default="https://hub.meltano.com",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapMeltanoHub.cli()
