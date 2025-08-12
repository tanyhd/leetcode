import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.numberOfWays(Solution, 10, 2), 1)

    def test_case_2(self):
        self.assertEqual(self.sol.numberOfWays(Solution, 4, 1), 2)


if __name__ == "__main__":
    unittest.main()