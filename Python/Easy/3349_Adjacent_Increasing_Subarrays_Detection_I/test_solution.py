import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.hasIncreasingSubarrays(Solution, [2,5,7,8,9,2,3,4,3,1], 3), True)

    def test_case_2(self):
        self.assertEqual(self.sol.hasIncreasingSubarrays(Solution, [1,2,3,4,4,4,4,5,6,7], 5), False)
        
    def test_case_3(self):
        self.assertEqual(self.sol.hasIncreasingSubarrays(Solution, [5,8,-2,-1], 2), True)

    def test_case_4(self):
        self.assertEqual(self.sol.hasIncreasingSubarrays(Solution, [-3,-19,-8,-16], 2), False)

    def test_case_5(self):
        self.assertEqual(self.sol.hasIncreasingSubarrays(Solution, [6,13,-17,-20,2], 2), False)

    def test_case_6(self):
        self.assertEqual(self.sol.hasIncreasingSubarrays(Solution, [-15,19], 1), True)


if __name__ == "__main__":
    unittest.main()