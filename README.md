# tap-meltanohub

`tap-meltanohub` is a Singer tap for MeltanoHub.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh  # or see https://docs.astral.sh/uv/getting-started/installation/
uv tool install git+https://github.com/MeltanoLabs/tap-meltanohub.git
```

## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-meltanohub --about
```

### Source Authentication and Authorization

## Usage

You can easily run `tap-meltanohub` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-meltanohub --version
tap-meltanohub --help
tap-meltanohub --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
uv sync
```

### Create and Run Tests

Create tests within the `tap_meltanohub/tests` subfolder and
  then run:

```bash
uv run pytest
```

You can also test the `tap-meltanohub` CLI interface directly using `uv run`:

```bash
uv run tap-meltanohub --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
uv tool install meltano
# Initialize meltano within this directory
cd tap-meltanohub
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-meltanohub --version
# OR run a test EL pipeline:
meltano run tap-meltanohub target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
