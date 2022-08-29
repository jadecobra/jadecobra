import src.jadecobra.toolkit
import unittest


class TestBuildDeploy(src.jadecobra.toolkit.TestCase):

    def test_build_and_publish(self):
        self.build_and_publish()