"""Stream type classes for tap-meltanohub."""

import importlib.resources

from tap_meltanohub.client import MeltanoStream
from tap_meltanohub import schemas

SCHEMAS_DIR = importlib.resources.files(schemas)


class MeltanoPlugins(MeltanoStream):
    """Define custom stream."""

    name = "plugins"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "plugins.json"
