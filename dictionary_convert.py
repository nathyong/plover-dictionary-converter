"""
Usage: python3 dictionary_convert.py [SOURCE_DICTIONARY] [OUTPUT_JSON]
"""
import sys

import json
from pathlib import Path

from plover import system
from plover.registry import registry
from plover.dictionary.base import create_dictionary, load_dictionary

import logging

logging.basicConfig(level=logging.DEBUG)

from plover_digitalcat_dictionary import DigitalCATDictionary

registry.register_plugin("dictionary", "dct", DigitalCATDictionary)

registry.update()
system.setup("English Stenotype")

input = sys.argv[1]
output = sys.argv[2]

id = load_dictionary(input)

Path(output).write_text(
    json.dumps(
        {"/".join(k): v.strip() for k, v in id._contents.items()},
        indent=0,
        sort_keys=True,
    )
)

# od = create_dictionary(output)
# od.update(id)
# od.save()
