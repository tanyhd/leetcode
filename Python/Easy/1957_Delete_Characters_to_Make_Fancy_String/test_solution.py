import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.makeFancyString(Solution, "leeetcode"), "leetcode")

    def test_case_2(self):
        self.assertEqual(self.sol.makeFancyString(Solution, "aaabaaaa"), "aabaa")

    def test_case_3(self):
        self.assertEqual(self.sol.makeFancyString(Solution, "aab"), "aab")


if __name__ == "__main__":
    unittest.main()