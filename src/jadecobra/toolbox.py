import datetime
import pathlib
import time
import os
import json
import unittest


class TestCase(unittest.TestCase):

    maxDiff = None

    @staticmethod
    def get_template(filepath):
        with open(f'{filepath}.template.json') as template:
            return json.load(template)

    def assert_cdk_templates_equal(self, stack_name):
        self.assertEqual(
            self.get_template(f"cdk.out/{stack_name}"),
            self.get_template(f"tests/fixtures/{stack_name}")
        )

    def assert_attributes_equal(self, thing=None, attributes=None):
        self.assertEqual(sorted(dir(thing)), attributes)


def logger(message, level="INFO"):
    print(f"[{level}] {message}")

def error(message):
    logger(message, level="ERROR")

def delete(filepath):
    try:
        os.remove(filepath)
    except FileNotFoundError:
        f"Could not find {filepath}"

def file_exists(filepath):
    return pathlib.Path(filepath).exists()

def make_dir(filepath):
    try:
        os.makedirs(pathlib.Path(filepath).parent)
    except FileExistsError:
        pass

def write_config(filepath, parser):
    "Write Config Parameters to filepath"
    make_dir(filepath)
    with open(filepath, "w") as configfile:
        parser.write(configfile)

def write_file(filepath, data):
    "Write Credentials to filepath"
    filepath = filepath.replace('\\', '/')
    make_dir(filepath)
    logger(f"Writing data to {filepath}")
    with open(filepath, "w") as writer:
        writer.write(str(data))

def delimiter():
    print("="*80)

def log(message):
    print(f"{datetime.datetime.now()}::{message}\n")

def header(environment):
    delimiter()
    print(f"\t[WARNING] You are making changes to the {environment} Environment [WARNING]")
    delimiter()

def time_it(function, *args, description='run process', **kwargs):
    start_time = time.time()
    function(*args, **kwargs)
    log(f'Time taken to {description}::{time.time() - start_time:.1f} seconds')