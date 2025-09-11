import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertAlmostEqual(self.sol.sortVowels(Solution, "lEetcOde"), "lEOtcede")

    def test_case_2(self):
        self.assertAlmostEqual(self.sol.sortVowels(Solution, "lYmpH"), "lYmpH")

if __name__ == "__main__":
    unittest.main()