import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.minCost(Solution, "abaac", [1,2,3,4,5]), 3)

    def test_case_2(self):
        self.assertEqual(self.sol.minCost(Solution, "abc", [1,2,3]), 0)
    
    def test_case_3(self):
        self.assertEqual(self.sol.minCost(Solution, "aabaa", [1,2,3,4,1]), 2)

    def test_case_4(self):
        self.assertEqual(self.sol.minCost(Solution, "aaabbbabbbb", [3,5,10,7,5,3,5,5,4,8,1]), 26)


if __name__ == "__main__":
    unittest.main()