import os
import unittest
os.system('pip install -r requirements.txt')


class TestBuild(unittest.TestCase):

    def test_z_build(self):
        return
        os.system('python3 -m build')
        # os.system('python3 -m twine upload dist/*')