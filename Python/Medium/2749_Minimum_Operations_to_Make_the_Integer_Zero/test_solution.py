import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.makeTheIntegerZero(Solution, 3, -2), 3)

    def test_case_2(self):
        self.assertEqual(self.sol.makeTheIntegerZero(Solution, 5, 7), -1)


if __name__ == "__main__":
    unittest.main()