import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.largestTriangleArea(Solution, [[0,0],[0,1],[1,0],[0,2],[2,0]]), 2.0)

    def test_case_2(self):
        self.assertEqual(self.sol.largestTriangleArea(Solution, [[1,0],[0,0],[0,1]]), 0.5)

if __name__ == "__main__":
    unittest.main()