import src.jadecobra.aws.lambda_deployer.deploy_lambda_layer
import src.jadecobra.toolkit

class TestAwsDeployLambdaLayer(src.jadecobra.toolkit.TestCase):

    def test_deploy_lambda_layer(self):
        with self.assertRaises(FileNotFoundError):
            src.jadecobra.aws.lambda_deployer.deploy_lambda_layer.LambdaLayer(
                dependencies=['bob_layer']
            )

    def test_deploy_lambda_layer_attributes(self):
        self.assert_attributes_equal(
            src.jadecobra.aws.lambda_deployer.deploy_lambda_layer.LambdaLayer,
            [
                '__class__',
                '__delattr__',
                '__dict__',
                '__dir__',
                '__doc__',
                '__eq__',
                '__format__',
                '__ge__',
                '__getattribute__',
                '__gt__',
                '__hash__',
                '__init__',
                '__init_subclass__',
                '__le__',
                '__lt__',
                '__module__',
                '__ne__',
                '__new__',
                '__reduce__',
                '__reduce_ex__',
                '__repr__',
                '__setattr__',
                '__sizeof__',
                '__str__',
                '__subclasshook__',
                '__weakref__',
                'delete_directory',
                'delete_previous_layer_version',
                'delete_zipfile',
                'delimiter',
                'directory',
                'get_layer_versions',
                'install_dependencies',
                'package_layer',
                'publish_layer',
                'runtime',
                's3_key',
                'set_name',
                'upload_to_s3',
                'zip_filename'
            ]
        )