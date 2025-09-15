import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.canBeTypedWords(Solution, "hello world", "ad"), 1)

    def test_case_2(self):
        self.assertEqual(self.sol.canBeTypedWords(Solution, "leet code", "lt"), 1)
    
    def test_case_3(self):
        self.assertEqual(self.sol.canBeTypedWords(Solution, "leet code", "e"), 0)


if __name__ == "__main__":
    unittest.main()