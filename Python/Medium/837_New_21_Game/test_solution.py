import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertAlmostEqual(self.sol.new21Game(Solution, 10, 1, 10), 1.00000, delta=1e-5)

    def test_case_2(self):
        self.assertAlmostEqual(self.sol.new21Game(Solution, 6,1,10), 0.60000, delta=1e-5)

    def test_case_3(self):
        self.assertAlmostEqual(self.sol.new21Game(Solution, 21,17,10), 0.73278, delta=1e-5)


if __name__ == "__main__":
    unittest.main()