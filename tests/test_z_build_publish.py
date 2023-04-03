import src.jadecobra.tester
import src.jadecobra.versioning
import os

class TestZBuildDeploy(src.jadecobra.tester.TestCase):

    version = src.jadecobra.versioning.Version()

    # def test_update_version(self):
    #     self.assertEqual(
    #         self.version.get_pyproject_version(),
    #         ('0.3.', '7'),
    #     )

    def test_z_build_and_publish(self):
        self.version.build_and_publish()

    def test_z_published_version_is_test_version(self):
        os.system('pip install jadecobra')
        import jadecobra
        self.assertEqual(
            jadecobra.__version__,
            src.jadecobra.__version__
        )