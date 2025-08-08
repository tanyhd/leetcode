import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.soupServings(Solution, 50), 0.62500)

    def test_case_2(self):
        self.assertEqual(self.sol.soupServings(Solution, 100), 0.71875)

if __name__ == "__main__":
    unittest.main()