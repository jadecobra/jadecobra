import unittest
import boto3
import jadecobra.aws.deploy_lambda_function
import jadecobra.aws.deploy_lambda
import jadecobra.aws.deploy_lambda_layer
import src.jadecobra.aws.deploy
import src.jadecobra.

class TestAwsLambdaTools(unittest.TestCase):

    def test_lambda_deployer(self):
        src.jadecobra.aws.deploy_lambda.LambdaDeployer()

    def test_lambda_deployer_attributes(self):
        self.assertEqual(
            sorted(dir(src.jadecobra.aws.deploy_lambda.LambdaDeployer)),
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
                'delete_zipfile',
                'delimiter',
                's3_key',
                'upload_to_s3'
            ]
        )

    def test_lambda_function(self):
        with self.assertRaises(TypeError):
            src.jadecobra.aws.deploy_lambda_function.LambdaFunction(
                function_name='bob_function'
            )

    def test_lambda_function_attributes(self):
        self.assertEqual(
            sorted(dir())
        )

    def test_lambda_layer(self):
        with self.assertRaises(TypeError):
            src.jadecobra.aws.deploy_lambda_layer.LambdaLayer(
                dependencies='bob_layer'
            )