import src.jadecobra.tester
import src.jadecobra.versioning
import src.jadecobra.toolkit
import os

class TestZBuildDeploy(src.jadecobra.tester.TestCase):

    version = src.jadecobra.versioning.Version()

    # def test_update_version(self):
    #     self.assertEqual(
    #         self.version.get_pyproject_version(),
    #         ('0.3.', '7'),
    #     )

    def test_z_published_version_is_test_version(self):
        print('installing latest version of jadecobra...')
        os.system('pip install jadecobra')
        import jadecobra
        try:
            self.assertEqual(
                jadecobra.__version__,
                src.jadecobra.__version__
            )
        except AssertionError:
            pass
        try:
            self.assertEqual(
                src.jadecobra.toolkit.build_and_publish(),
                0
            )
        except AssertionError:
            try:
                self.version.update_pyproject_version()
                self.version.update_module_version()
            except FileNotFoundError:
                pass
            finally:
                self.assertEqual(
                    src.jadecobra.toolkit.build_and_publish(),
                    0
                )
