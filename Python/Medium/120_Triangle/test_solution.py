import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.minimumTotal(Solution, [[2],[3,4],[6,5,7],[4,1,8,3]]), 11)

    def test_case_2(self):
        self.assertEqual(self.sol.minimumTotal(Solution, [[-10]]), -10)
    
if __name__ == "__main__":
    unittest.main()