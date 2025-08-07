import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maximumGain(Solution, "cdbcbbaaabab", 4, 5), 19)

    def test_case_2(self):
        self.assertEqual(self.sol.maximumGain(Solution, "aabbaaxybbaabb", 5, 4), 20)


if __name__ == "__main__":
    unittest.main()