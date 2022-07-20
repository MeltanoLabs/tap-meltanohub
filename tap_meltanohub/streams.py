"""Stream type classes for tap-meltanohub."""

from pathlib import Path

from tap_meltanohub.client import MeltanoStream, SingerStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class SingerTaps(SingerStream):
    """Define custom stream."""

    name = "taps"
    path = "/taps.json"
    primary_keys = ["name"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "tap.json"


class MeltanoPlugins(MeltanoStream):
    """Define custom stream."""

    name = "plugins"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "plugins.json"
