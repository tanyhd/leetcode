import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.isPowerOfThree(Solution, 27), True)

    def test_case_2(self):
        self.assertEqual(self.sol.isPowerOfThree(Solution, 0), False)

    def test_case_3(self):
        self.assertEqual(self.sol.isPowerOfThree(Solution, -1), False)


if __name__ == "__main__":
    unittest.main()