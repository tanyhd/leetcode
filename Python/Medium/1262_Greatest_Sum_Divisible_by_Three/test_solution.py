import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maxSumDivThree(Solution, [3,6,5,1,8]), 18)

    def test_case_2(self):
        self.assertEqual(self.sol.maxSumDivThree(Solution, [4]), 0)
    
    def test_case_3(self):
        self.assertEqual(self.sol.maxSumDivThree(Solution, [1,2,3,4,4]), 12)


if __name__ == "__main__":
    unittest.main()