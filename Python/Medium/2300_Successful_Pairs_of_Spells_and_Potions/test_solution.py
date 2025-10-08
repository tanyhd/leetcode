import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.successfulPairs(Solution, [5,1,3], [1,2,3,4,5], 7), [4,0,3])

    def test_case_2(self):
        self.assertEqual(self.sol.successfulPairs(Solution, [3,1,2], [8,5,8], 16), [2,0,2])

    def test_case_3(self):
        self.assertEqual(self.sol.successfulPairs(Solution, [15,8,19], [38,36,23], 328), [3,0,3])


if __name__ == "__main__":
    unittest.main()