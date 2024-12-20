import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner('Anna')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Anna')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner, runner2 = Runner('Anna'), Runner('Dima')
        for _ in range(10):
            runner.run()
            runner2.walk()
        self.assertNotEqual(runner.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()