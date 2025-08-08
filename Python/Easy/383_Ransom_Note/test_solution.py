import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.canConstruct(Solution, "a", "b"), False)

    def test_case_2(self):
        self.assertEqual(self.sol.canConstruct(Solution, "aa", "ab"), False)

    def test_case_3(self):
        self.assertEqual(self.sol.canConstruct(Solution, "aa", "aab"), True)


if __name__ == "__main__":
    unittest.main()