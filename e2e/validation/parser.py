import os
import yaml

"""
Some useful functions 
"""


def get_template(schema):
    base = f"{os.path.abspath(os.path.dirname(__file__))}"
    with open(f"{base}/schemas.yaml") as data_file:
        data = yaml.safe_load(data_file)
    return data['schemas'][schema]


def get_limit_value(limit):
    return int(str(limit.split("=")[1]))
