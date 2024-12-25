import unittest
from main_code import Runner
import logging as lg


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        lg.basicConfig(level=lg.INFO,
                       filemode='w',
                       filename='runner_tests.log',
                       format="%(asctime)s | %(levelname)s | %(message)s",
                       encoding='utf-8')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        try:
            runner = Runner('Anna', -10)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            lg.info('test_walk выполнен успешно')
        except ValueError:
            lg.warning('Неверная скорость для Runner.', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        try:
            runner = Runner(4, 10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 200)
            lg.info('test_run выполнен успешно')
        except TypeError:
            lg.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        runner, runner2 = Runner('Anna'), Runner('Dima')
        for _ in range(10):
            runner.run()
            runner2.walk()
        self.assertNotEqual(runner.distance, runner2.distance)
        lg.info('test_challenge выполнен успешно.')

if __name__ == '__main__':
    unittest.main()