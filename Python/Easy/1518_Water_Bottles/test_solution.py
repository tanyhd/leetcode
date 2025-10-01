import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.numWaterBottles(Solution, 9, 3), 13)

    def test_case_2(self):
        self.assertEqual(self.sol.numWaterBottles(Solution,15, 4), 19)
    
    def test_case_3(self):
        self.assertEqual(self.sol.numWaterBottles(Solution, 5, 5), 6)


if __name__ == "__main__":
    unittest.main()