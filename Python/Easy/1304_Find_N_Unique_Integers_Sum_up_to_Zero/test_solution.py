import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(sum(self.sol.sumZero(Solution, 5)), 0)

    def test_case_2(self):
        self.assertEqual(sum(self.sol.sumZero(Solution, 3)), 0)

    def test_case_3(self):
        self.assertEqual(sum(self.sol.sumZero(Solution, 1)), 0)


if __name__ == "__main__":
    unittest.main()