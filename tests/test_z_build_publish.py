import src.jadecobra.tester
import src.jadecobra.versioning
import src.jadecobra.toolkit
import os

class TestZBuildDeploy(src.jadecobra.tester.TestCase):

    version = src.jadecobra.versioning.Version()

    def test_z_published_version_is_test_version(self):
        print('installing latest version of jadecobra...')
        os.system('pip install jadecobra')
        import jadecobra
        self.assertEqual(
            jadecobra.__version__,
            src.jadecobra.__version__
        )
        self.assertEqual(
            jadecobra.__version__,
            self.version.current_pyproject_version
        )
        try:
            self.assertEqual(
                src.jadecobra.toolkit.publish(True),
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
                    src.jadecobra.toolkit.publish(True),
                    0
                )
                print('installing latest version of jadecobra...')
                os.system('pip install jadecobra')
                import jadecobra
                self.assertEqual(
                    jadecobra.__version__,
                    src.jadecobra.__version__
                )
                self.assertEqual(
                    jadecobra.__version__,
                    self.version.current_pyproject_version
                )