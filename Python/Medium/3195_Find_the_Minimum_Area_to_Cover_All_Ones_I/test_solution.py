import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.minimumArea(Solution, [[0,1,0],[1,0,1]]), 6)

    def test_case_2(self):
        self.assertEqual(self.sol.minimumArea(Solution, [[1,0],[0,0]]), 1)
    
    def test_case_3(self):
        self.assertEqual(self.sol.minimumArea(Solution, [[0],[1]]), 1)


if __name__ == "__main__":
    unittest.main()