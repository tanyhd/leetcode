import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.processQueries(Solution, 5, [[1,2],[2,3],[3,4],[4,5]], [[1,3],[2,1],[1,1],[2,2],[1,2]]), [3,2,3])

    def test_case_2(self):
        self.assertEqual(self.sol.processQueries(Solution, 3, [], [[1,1],[2,1],[1,1]]), [1,-1])
    
    def test_case_3(self):
        self.assertEqual(self.sol.processQueries(Solution, 1, [], [[1,1],[2,1],[2,1],[2,1],[2,1]]), [1])

    def test_case_4(self):
        self.assertEqual(self.sol.processQueries(Solution, 4, [[4,3],[3,1],[4,2],[3,2],[4,1]],  [[2,3],[1,2],[2,4],[1,1],[2,2],[1,2],[1,2],[2,2],[1,3],[2,3],[2,4],[2,3],[2,4],[1,2],[1,1]]), [2,1,1,1,1,1,1])


if __name__ == "__main__":
    unittest.main()