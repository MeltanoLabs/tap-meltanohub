"""Stream type classes for tap-meltanohub."""

from pathlib import Path

from tap_meltanohub.client import MeltanoStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class MeltanoPlugins(MeltanoStream):
    """Define custom stream."""

    name = "plugins"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "plugins.json"
