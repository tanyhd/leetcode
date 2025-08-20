import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.countSquares(Solution, [[0,1,1,1],[1,1,1,1],[0,1,1,1]]), 15)

    def test_case_2(self):
        self.assertEqual(self.sol.countSquares(Solution, [[1,0,1],[1,1,0],[1,1,0]]), 7)


if __name__ == "__main__":
    unittest.main()