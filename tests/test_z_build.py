import os
import unittest
import shutil


class TestBuild(unittest.TestCase):

    @staticmethod
    def remove_dist():
        try:
            shutil.rmtree('dist')
        except FileNotFoundError:
            'already removed'

    def test_z_build(self):
        return
        self.remove_dist()
        os.system('python3 -m build')
        os.system('python3 -m twine upload dist/*')