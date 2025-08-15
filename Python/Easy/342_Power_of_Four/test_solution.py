import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.isPowerOfFour(Solution, 16), True)

    def test_case_2(self):
        self.assertEqual(self.sol.isPowerOfFour(Solution, 5), False)

    def test_case_3(self):
        self.assertEqual(self.sol.isPowerOfFour(Solution, 1), True)


if __name__ == "__main__":
    unittest.main()