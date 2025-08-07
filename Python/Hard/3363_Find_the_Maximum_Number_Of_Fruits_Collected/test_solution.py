import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maxCollectedFruits(Solution, [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]), 100)

    def test_case_2(self):
        self.assertEqual(self.sol.maxCollectedFruits(Solution, [[1,1],[1,1]]), 4)


if __name__ == "__main__":
    unittest.main()