import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.usein = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        participants =((self.usein, self.nick), (self.andrey, self.nick), (self.usein, self.andrey, self.nick))
        tournaments = (Tournament(90, *p) for p in participants)
        for t in tournaments:
            result = t.start()
            self.all_results.append(result)
            speeds = [r.speed for r in result.values()]
            self.assertListEqual(list1=speeds, list2=sorted(speeds, reverse=True))


if __name__ == '__main__':
    unittest.main()