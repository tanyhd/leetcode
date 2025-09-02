import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.numberOfPairs(Solution, [[1,1],[2,2],[3,3]]), 0)

    def test_case_2(self):
        self.assertEqual(self.sol.numberOfPairs(Solution, [[6,2],[4,4],[2,6]]), 2)
    
    def test_case_3(self):
        self.assertEqual(self.sol.numberOfPairs(Solution, [[3,1],[1,3],[1,1]]), 2)


if __name__ == "__main__":
    unittest.main()