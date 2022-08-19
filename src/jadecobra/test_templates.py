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
