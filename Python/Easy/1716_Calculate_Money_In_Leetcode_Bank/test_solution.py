import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.totalMoney(Solution, 4), 10)

    def test_case_2(self):
        self.assertEqual(self.sol.totalMoney(Solution, 10), 37)
    
    def test_case_3(self):
        self.assertEqual(self.sol.totalMoney(Solution, 20), 96)


if __name__ == "__main__":
    unittest.main()