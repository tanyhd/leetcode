import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertAlmostEqual(self.sol.triangularSum(Solution, [1,2,3,4,5]), 8)

    def test_case_2(self):
        self.assertAlmostEqual(self.sol.triangularSum(Solution, [5]), 5)

if __name__ == "__main__":
    unittest.main()