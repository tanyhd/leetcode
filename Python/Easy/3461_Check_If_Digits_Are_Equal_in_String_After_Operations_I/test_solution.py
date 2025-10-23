import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.hasSameDigits(Solution, "3902"), True)

    def test_case_2(self):
        self.assertEqual(self.sol.hasSameDigits(Solution, "34789"), False)


if __name__ == "__main__":
    unittest.main()