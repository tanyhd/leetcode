import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.nextBeautifulNumber(Solution, 1), 22)

    def test_case_2(self):
        self.assertEqual(self.sol.nextBeautifulNumber(Solution, 1000), 1333)

    def test_case_3(self):
        self.assertEqual(self.sol.nextBeautifulNumber(Solution, 3000), 3133)

    def test_case_4(self):
        self.assertEqual(self.sol.nextBeautifulNumber(Solution, 212), 221)

if __name__ == "__main__":
    unittest.main()