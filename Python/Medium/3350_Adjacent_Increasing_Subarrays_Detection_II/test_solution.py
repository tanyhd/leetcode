import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertAlmostEqual(self.sol.maxIncreasingSubarrays(Solution, [2,5,7,8,9,2,3,4,3,1]), 3)

    def test_case_2(self):
        self.assertAlmostEqual(self.sol.maxIncreasingSubarrays(Solution, [1,2,3,4,4,4,4,5,6,7]), 2)
    
    def test_case_3(self):
        self.assertAlmostEqual(self.sol.maxIncreasingSubarrays(Solution, [-15,19]), 1)


if __name__ == "__main__":
    unittest.main()