import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maxFreqSum(Solution, "successes"), 6)

    def test_case_2(self):
        self.assertEqual(self.sol.maxFreqSum(Solution, "aeiaeia") , 3)

if __name__ == "__main__":
    unittest.main()