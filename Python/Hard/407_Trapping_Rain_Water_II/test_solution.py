import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.trapRainWater(Solution, [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]), 4)

    def test_case_2(self):
        self.assertEqual(self.sol.trapRainWater(Solution, [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]), 10)

if __name__ == "__main__":
    unittest.main()