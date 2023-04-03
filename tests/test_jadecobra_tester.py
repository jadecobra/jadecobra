import src.jadecobra
import src.jadecobra.tester


class TestJadeCobraTester(src.jadecobra.tester.TestCase):

    def test_tester_attributes(self):
        self.assert_attributes_equal(
            src.jadecobra.tester,
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
                'json',
                'os',
                'shutil',
                'subprocess',
                'toolkit',
                'unittest',
                'versioning'
            ]
        )

    def test_tester_test_case_attributes(self):
        self.assert_attributes_equal(
            src.jadecobra.tester.TestCase,
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
                '__getstate__',
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
                'build_and_publish',
                'countTestCases',
                'create_cdk_templates',
                'debug',
                'defaultTestResult',
                'doClassCleanups',
                'doCleanups',
                'enterClassContext',
                'enterContext',
                'fail',
                'failIf',
                'failIfAlmostEqual',
                'failIfEqual',
                'failUnless',
                'failUnlessAlmostEqual',
                'failUnlessEqual',
                'failUnlessRaises',
                'failureException',
                'id',
                'longMessage',
                'maxDiff',
                'read_json',
                'remove_dist',
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
