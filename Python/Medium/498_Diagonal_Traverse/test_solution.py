import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.findDiagonalOrder(Solution, [[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9])

    def test_case_2(self):
        self.assertEqual(self.sol.findDiagonalOrder(Solution, [[1,2],[3,4]]), [1,2,3,4])

if __name__ == "__main__":
    unittest.main()