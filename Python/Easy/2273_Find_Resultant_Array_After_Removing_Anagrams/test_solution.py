import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.removeAnagrams(Solution, ["abba","baba","bbaa","cd","cd"]), ["abba","cd"])

    def test_case_2(self):
        self.assertEqual(self.sol.removeAnagrams(Solution,["a","b","c","d","e"]), ["a","b","c","d","e"])

if __name__ == "__main__":
    unittest.main()