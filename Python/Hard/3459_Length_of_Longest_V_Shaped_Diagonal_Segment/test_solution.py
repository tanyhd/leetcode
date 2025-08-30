import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.lenOfVDiagonal(Solution, [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]), 5)

    def test_case_2(self):
        self.assertEqual(self.sol.lenOfVDiagonal(Solution, [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]), 4)
    
    def test_case_3(self):
        self.assertEqual(self.sol.lenOfVDiagonal(Solution, [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]), 5)
    
    def test_case_4(self):
        self.assertEqual(self.sol.lenOfVDiagonal(Solution, [[1]]), 1)
    
    def test_case_5(self):
        self.assertEqual(self.sol.lenOfVDiagonal(Solution, [[0,0,1,0],[0,2,2,0]]), 3)
    
    def test_case_6(self):
        self.assertEqual(self.sol.lenOfVDiagonal(Solution, [[1,1,1,2,0,0],[0,0,0,0,1,2]]), 2)


if __name__ == "__main__":
    unittest.main()