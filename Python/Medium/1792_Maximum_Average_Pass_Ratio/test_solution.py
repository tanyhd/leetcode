import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertAlmostEqual(self.sol.maxAverageRatio(Solution, [[1,2],[3,5],[2,2]], 2), 0.78333, delta=1e-5)

    def test_case_2(self):
        self.assertAlmostEqual(self.sol.maxAverageRatio(Solution, [[2,4],[3,9],[4,5],[2,10]], 4), 0.53485, delta=1e-5)


if __name__ == "__main__":
    unittest.main()