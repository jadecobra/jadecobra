import subprocess
import unittest

from . import toolkit


class TestCase(unittest.TestCase):

    maxDiff = None

    def create_cdk_templates(self):
        '''Create CloudFormation using CDK with presets'''
        result = toolkit.time_it(
            (
                'cdk ls '
                '--no-version-reporting '
                '--no-path-metadata '
                '--no-asset-metadata'
            ),
            function=subprocess.run,
            description=f'cdk ls',
            shell=True,
            capture_output=True,
        )
        print(result.stderr.decode())
        print(result.stdout.decode())
        self.assertEqual(result.returncode, 0)

    def assert_cdk_templates_equal(self, stack_name):
        '''Check if stack_name in cdk.out folder and tests/fixtures are the same'''
        self.assertEqual(
            toolkit.read_json(f"cdk.out/{stack_name}"),
            toolkit.read_json(f"tests/fixtures/{stack_name}")
        )

    def assert_attributes_equal(self, thing=None, attributes=None):
        '''Check that the given attributes match the attributes of thing'''
        self.assertEqual(
            sorted(dir(thing)), sorted(attributes)
        )