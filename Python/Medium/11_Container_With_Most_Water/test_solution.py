import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maxArea(Solution, [1,8,6,2,5,4,8,3,7]), 49)

    def test_case_2(self):
        self.assertEqual(self.sol.maxArea(Solution, [1,1]), 1)
    
if __name__ == "__main__":
    unittest.main()