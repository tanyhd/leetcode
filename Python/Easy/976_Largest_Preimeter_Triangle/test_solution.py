import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.largestPerimeter(Solution, [2,1,2]), 5)

    def test_case_2(self):
        self.assertEqual(self.sol.largestPerimeter(Solution, [1,2,1,10]), 0)

if __name__ == "__main__":
    unittest.main()