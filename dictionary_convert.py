"""
Usage: python3 dictionary_convert.py [INPUT_DICTIONARY] [OUTPUT_JSON]
"""

from pathlib import Path
import argparse
import json
import logging
import sys

from plover import system
from plover.registry import registry
from plover.dictionary.base import create_dictionary, load_dictionary

_LOG = logging.getLogger(__file__)

try:
    from plover_digitalcat_dictionary import DigitalCATDictionary

    registry.register_plugin("dictionary", "dct", DigitalCATDictionary)
except ImportError:
    _LOG.warning("Could not load DigitalCATDictionary support")


if __name__ == "__main__":
    # Required to load dictionary support in general
    registry.update()
    system.setup("English Stenotype")

    ap = argparse.ArgumentParser()
    ap.add_argument("input_dictionary", help="Path to the input dictionary", type=Path)
    ap.add_argument("output_json", help="Path to the output JSON file", type=Path)
    opts = ap.parse_args()

    id = load_dictionary(str(opts.input_dictionary))

    # dump from the input dictionary directly
    opts.output_json.write_text(
        json.dumps(
            {"/".join(k): v.strip() for k, v in id._dict.items()},
            indent=0,
            sort_keys=True,
        )
    )
