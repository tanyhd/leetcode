import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.swimInWater(Solution, [[0,2],[1,3]]), 3)

    def test_case_2(self):
        self.assertEqual(self.sol.swimInWater(Solution, [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]), 16)


if __name__ == "__main__":
    unittest.main()