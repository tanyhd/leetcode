import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maximumTotalDamage(Solution, [1,1,3,4]), 6)

    def test_case_2(self):
        self.assertEqual(self.sol.maximumTotalDamage(Solution, [7,1,6,6]), 13)

if __name__ == "__main__":
    unittest.main()