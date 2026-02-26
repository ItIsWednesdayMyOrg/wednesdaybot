import os
from datetime import datetime

import yaml


def load_quotes(path="./wednesda.yaml"):
    with open(path) as f:
        wednesday_list = yaml.safe_load(f)
    return [
        {
            "quote": item["Text"],
            "attribution": item.get("Attribution") or "",
        }
        for item in wednesday_list
    ]


def is_it_wednesday(fake_wednesday=False):
    pretend_its_wednesday = fake_wednesday
    if os.environ.get("FAKE_WEDNESDAY", ""):
        pretend_its_wednesday = True
    if not pretend_its_wednesday:
        today = datetime.now()
        if today.weekday() != 2:
            return False
    return True
