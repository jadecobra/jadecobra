import re
import os

from . import toolkit


class Version(object):

    def __init__(self):
        self.text = self.read_pyproject()
        self.version, self.patch = self.get_pyproject_version()
        self.new_version = f"{self.version}{int(self.patch)+1}"

    @staticmethod
    def pyproject():
        return 'pyproject.toml'

    @staticmethod
    def semantic_version_pattern():
        return r'version\s+=\s+"(\d+[.]\d+[.])(\d+)"'

    def read_pyproject(self):
        '''Return contents of file'''
        with open(self.pyproject()) as file:
            return file.read()

    def get_pyproject_version(self):
        '''Get version from pyproject.toml'''
        return re.search(
            self.semantic_version_pattern(),
            self.text
        ).group(1, 2)

    def update_pyproject_version(self):
        '''Update version in pyproject.toml'''
        toolkit.write_file(
            filepath=self.pyproject(),
            data=re.sub(
                self.semantic_version_pattern(),
                f'version = "{self.new_version}"',
                self.text
            )
        )

    def update_module_version(self):
        '''Update Module Version'''
        toolkit.write_file(
            filepath='src/jadecobra/__init__.py',
            data=f'__version__ = "{self.new_version}"',
        )

    def git_push(self):
        '''Update version for project and push upstream'''
        try:
            self.update_pyproject_version()
            self.update_module_version()
        except FileNotFoundError:
            pass
        finally:
            os.system(f'git commit -am "{toolkit.get_commit_message()}"')
            os.system('git push')

    def build_and_publish(self):
        '''Build the python distribution and upload to pypi'''
        self.git_push()
        self.remove_dist()
        os.system('python3 -m build')
        self.assertEqual(
            os.system('python3 -m twine upload dist/*'), 0
        )
