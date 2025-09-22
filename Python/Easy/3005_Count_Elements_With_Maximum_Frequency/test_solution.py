import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maxFrequencyElements(Solution, [1,2,2,3,1,4]), 4)

    def test_case_2(self):
        self.assertEqual(self.sol.maxFrequencyElements(Solution, [1,2,3,4,5]), 5)


if __name__ == "__main__":
    unittest.main()