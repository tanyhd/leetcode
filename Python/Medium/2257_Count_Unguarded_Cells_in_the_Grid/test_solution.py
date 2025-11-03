import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.countUnguarded(Solution, 4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]), 7)

    def test_case_2(self):
        self.assertEqual(self.sol.countUnguarded(Solution, 3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]), 4)

if __name__ == "__main__":
    unittest.main()