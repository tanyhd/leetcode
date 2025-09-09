import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertAlmostEqual(self.sol.peopleAwareOfSecret(Solution, 6, 2, 4), 5)

    def test_case_2(self):
        self.assertAlmostEqual(self.sol.peopleAwareOfSecret(Solution, 4, 1, 3), 6)

    def test_case_3(self):
        self.assertAlmostEqual(self.sol.peopleAwareOfSecret(Solution, 4, 1, 4), 8)


if __name__ == "__main__":
    unittest.main()