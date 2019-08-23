import os
import unittest


def extend_suite(cases):
    for case in cases:
        suite.addTest(case)


suite = unittest.TestSuite()

if int(os.getenv('auth', '1')) == 1:
    from tests.test_authentication import TestAuth

    extend_suite([TestAuth])


def run():
    unittest.TextTestRunner(verbosity=2).run(suite)
