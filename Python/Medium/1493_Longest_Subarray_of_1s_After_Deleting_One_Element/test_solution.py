import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.longestSubarray(Solution, [1,1,0,1]), 3)
    
    def test_case_2(self):
        self.assertEqual(self.sol.longestSubarray(Solution, [0,1,1,1,0,1,1,0,1]), 5)

    def test_case_3(self):
        self.assertEqual(self.sol.longestSubarray(Solution, [1,1,1]), 2)


if __name__ == "__main__":
    unittest.main()