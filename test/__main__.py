from unittest import TestLoader, TextTestRunner, TestSuite

from test_parser import TestParser


if __name__ == '__main__':

    loader = TestLoader()
    tests = [
        loader.loadTestsFromTestCase(test)
        for test in (
            TestParser
        )
    ]
    suite = TestSuite(tests)

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)