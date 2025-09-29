import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.minScoreTriangulation(Solution, [1,2,3]), 6)

    def test_case_2(self):
        self.assertEqual(self.sol.minScoreTriangulation(Solution, [3,7,4,5]), 144)

    def test_case_3(self):
        self.assertEqual(self.sol.minScoreTriangulation(Solution, [1,3,1,4,1,5]), 13)


if __name__ == "__main__":
    unittest.main()