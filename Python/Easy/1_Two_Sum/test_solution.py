import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.twoSum(Solution, [2,7,11,15], 9), [0,1])

    def test_case_2(self):
        self.assertEqual(self.sol.twoSum(Solution, [3,2,4], 6), [1,2])

    def test_case_3(self):
        self.assertEqual(self.sol.twoSum(Solution, [3,3], 6), [0,1])


if __name__ == "__main__":
    unittest.main()