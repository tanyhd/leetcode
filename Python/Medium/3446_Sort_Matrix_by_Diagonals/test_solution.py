import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.sortMatrix(Solution, [[1,7,3],[9,8,2],[4,5,6]]), [[8,2,3],[9,6,7],[4,5,1]])

    def test_case_2(self):
        self.assertEqual(self.sol.sortMatrix(Solution, [[0,1],[1,2]]), [[2,1],[1,0]])
    
    def test_case_3(self):
        self.assertEqual(self.sol.sortMatrix(Solution, [[1]]), [[1]])


if __name__ == "__main__":
    unittest.main()