import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maxBottlesDrunk(Solution, 13, 6), 15)

    def test_case_2(self):
        self.assertEqual(self.sol.maxBottlesDrunk(Solution, 10, 3), 13)

if __name__ == "__main__":
    unittest.main()