import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.totalFruit(Solution, [1,2,1]), 3)

    def test_case_2(self):
        self.assertEqual(self.sol.totalFruit(Solution, [0,1,2,2]), 3)

    def test_case_3(self):
        self.assertEqual(self.sol.totalFruit(Solution, [1,2,3,2,2]), 4)


if __name__ == "__main__":
    unittest.main()