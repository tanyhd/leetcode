import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maxDistinctElements(Solution, [1,2,2,3,3,4], 2), 6)

    def test_case_2(self):
        self.assertEqual(self.sol.maxDistinctElements(Solution, [4,4,4,4], 1), 3)

if __name__ == "__main__":
    unittest.main()