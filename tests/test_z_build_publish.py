import importlib
import src.jadecobra.tester
import src.jadecobra.versioning
import src.jadecobra.toolkit
import os

def get_latest_published_version():
    library = 'jadecobra'
    print(f'installing latest version of {library}...')
    for command in (
        f'uninstall {library} -y',
        f'install {library}',
    ):
        os.system(f'pip {command}')

class TestZBuildDeploy(src.jadecobra.tester.TestCase):

    version = src.jadecobra.versioning.Version()

    def assert_published_version_is_source_version(self):
        get_latest_published_version()
        import jadecobra
        importlib.reload(jadecobra)
        self.assertEqual(
            jadecobra.__version__,
            src.jadecobra.__version__
        )
        self.assertEqual(
            jadecobra.__version__,
            self.version.current_pyproject_version
        )

    def test_z_published_version_is_test_version(self):
        # try:
        #     self.assert_published_version_is_source_version()
        # except AssertionError:
        try:
            self.assertEqual(
                src.jadecobra.toolkit.publish(True),
                0
            )
        except AssertionError:
            self.assertIsNone(
                src.jadecobra.toolkit.publish(True)
            )
            self.assert_published_version_is_source_version()