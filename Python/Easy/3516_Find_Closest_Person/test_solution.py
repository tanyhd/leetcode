import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.findClosest(Solution, 2, 7, 4), 1)

    def test_case_2(self):
        self.assertEqual(self.sol.findClosest(Solution, 2, 5, 6), 2)
    
    def test_case_3(self):
        self.assertEqual(self.sol.findClosest(Solution, 1, 5, 3), 0)


if __name__ == "__main__":
    unittest.main()