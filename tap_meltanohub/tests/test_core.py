"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_meltanohub.tap import TapMeltanoHub

SAMPLE_CONFIG = {"start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")}


TestTapMeltanoHub = get_tap_test_class(
    TapMeltanoHub,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(max_records_limit=20),
)
