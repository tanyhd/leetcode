import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.generate(Solution, 5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

    def test_case_2(self):
        self.assertEqual(self.sol.generate(Solution, 1), [[1]])


if __name__ == "__main__":
    unittest.main()