import unittest
import src.jadecobra.toolkit


class TestJadeCobra(src.jadecobra.toolkit.TestCase):

    def test_toolkit_test_case_attributes(self):
        self.assert_attributes_equal(
            src.jadecobra.toolkit.TestCase,
            [
                '__call__',
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
                '_addExpectedFailure',
                '_addSkip',
                '_addUnexpectedSuccess',
                '_baseAssertEqual',
                '_callCleanup',
                '_callSetUp',
                '_callTearDown',
                '_callTestMethod',
                '_classSetupFailed',
                '_class_cleanups',
                '_deprecate',
                '_diffThreshold',
                '_feedErrorsToResult',
                '_formatMessage',
                '_getAssertEqualityFunc',
                '_truncateMessage',
                'addClassCleanup',
                'addCleanup',
                'addTypeEqualityFunc',
                'assertAlmostEqual',
                'assertAlmostEquals',
                'assertCountEqual',
                'assertDictContainsSubset',
                'assertDictEqual',
                'assertEqual',
                'assertEquals',
                'assertFalse',
                'assertGreater',
                'assertGreaterEqual',
                'assertIn',
                'assertIs',
                'assertIsInstance',
                'assertIsNone',
                'assertIsNot',
                'assertIsNotNone',
                'assertLess',
                'assertLessEqual',
                'assertListEqual',
                'assertLogs',
                'assertMultiLineEqual',
                'assertNoLogs',
                'assertNotAlmostEqual',
                'assertNotAlmostEquals',
                'assertNotEqual',
                'assertNotEquals',
                'assertNotIn',
                'assertNotIsInstance',
                'assertNotRegex',
                'assertNotRegexpMatches',
                'assertRaises',
                'assertRaisesRegex',
                'assertRaisesRegexp',
                'assertRegex',
                'assertRegexpMatches',
                'assertSequenceEqual',
                'assertSetEqual',
                'assertTrue',
                'assertTupleEqual',
                'assertWarns',
                'assertWarnsRegex',
                'assert_',
                'assert_attributes_equal',
                'assert_cdk_templates_equal',
                'countTestCases',
                'debug',
                'defaultTestResult',
                'doClassCleanups',
                'doCleanups',
                'fail',
                'failIf',
                'failIfAlmostEqual',
                'failIfEqual',
                'failUnless',
                'failUnlessAlmostEqual',
                'failUnlessEqual',
                'failUnlessRaises',
                'failureException',
                'get_template',
                'id',
                'longMessage',
                'maxDiff',
                'run',
                'setUp',
                'setUpClass',
                'shortDescription',
                'skipTest',
                'subTest',
                'tearDown',
                'tearDownClass'
            ]
        )

    def test_toolkit(self):
        self.assert_attributes_equal(
            src.jadecobra.toolkit,
            [
                'TestCase',
                '__builtins__',
                '__cached__',
                '__doc__',
                '__file__',
                '__loader__',
                '__name__',
                '__package__',
                '__spec__',
                'build_and_publish',
                'datetime',
                'delete',
                'delimiter',
                'error',
                'file_exists',
                'header',
                'json',
                'log',
                'logger',
                'make_dir',
                'os',
                'pathlib',
                'remove_dist',
                'shutil',
                'time',
                'time_it',
                'unittest',
                'write_config',
                'write_file'
            ]
        )
