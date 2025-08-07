import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.numOfUnplacedFruits(Solution, [4,2,5], [3,5,4]), 1)

    def test_case_2(self):
        self.assertEqual(self.sol.numOfUnplacedFruits(Solution, [3,6,1], [6,4,7]), 0)


if __name__ == "__main__":
    unittest.main()