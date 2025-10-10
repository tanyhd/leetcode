import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maximumEnergy(Solution, [5,2,-10,-5,1], 3), 3)

    def test_case_2(self):
        self.assertEqual(self.sol.maximumEnergy(Solution, [-2,-3,-1], 2), -1)

if __name__ == "__main__":
    unittest.main()