import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertAlmostEqual(self.sol.doesAliceWin(Solution, "leetcoder"), True)

    def test_case_2(self):
        self.assertAlmostEqual(self.sol.doesAliceWin(Solution, "bbcd"), False)


if __name__ == "__main__":
    unittest.main()