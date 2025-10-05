import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.pacificAtlantic(Solution, [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]), [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])

    def test_case_2(self):
        self.assertEqual(self.sol.pacificAtlantic(Solution, [[1]]), [[0,0]])
    
    def test_case_3(self):
        self.assertEqual(self.sol.pacificAtlantic(Solution, [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]), [[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]])
    
    def test_case_4(self):
        self.assertEqual(self.sol.pacificAtlantic(Solution, [[10,10,10],[10,1,10],[10,10,10]]), [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]])

if __name__ == "__main__":
    unittest.main()