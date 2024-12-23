from u_module_12_1 import RunnerTest
from u_module_12_2 import TournamentTest
import unittest


test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
test_suite_run = unittest.TextTestRunner(verbosity=2)
test_suite_run.run(test_suite)