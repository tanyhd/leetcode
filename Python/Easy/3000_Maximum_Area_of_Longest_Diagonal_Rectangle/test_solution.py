import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.areaOfMaxDiagonal(Solution, [[9,3],[8,6]]), 48)

    def test_case_2(self):
        self.assertEqual(self.sol.areaOfMaxDiagonal(Solution,[[3,4],[4,3]]), 12)
    
    def test_case_3(self):
        self.assertEqual(self.sol.areaOfMaxDiagonal(Solution, [[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]), 20)


if __name__ == "__main__":
    unittest.main()