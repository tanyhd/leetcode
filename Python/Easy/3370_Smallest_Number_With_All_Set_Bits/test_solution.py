import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.smallestNumber(Solution, 5), 7)

    def test_case_2(self):
        self.assertEqual(self.sol.smallestNumber(Solution, 10), 15)
    
    def test_case_3(self):
        self.assertEqual(self.sol.smallestNumber(Solution, 3), 3)


if __name__ == "__main__":
    unittest.main()