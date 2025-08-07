import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maxSum(Solution, [1,2,3,4,5]), 15)

    def test_case_2(self):
        self.assertEqual(self.sol.maxSum(Solution, [1,1,0,1,1]), 1)
    
    def test_case_3(self):
        self.assertEqual(self.sol.maxSum(Solution, [1,2,-1,-2,1,0,-1]), 3)


if __name__ == "__main__":
    unittest.main()