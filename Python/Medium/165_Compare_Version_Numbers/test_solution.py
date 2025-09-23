import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.compareVersion(Solution, "1.2", "1.10"), -1)

    def test_case_2(self):
        self.assertEqual(self.sol.compareVersion(Solution, "1.01", "1.001"), 0)
    
    def test_case_3(self):
        self.assertEqual(self.sol.compareVersion(Solution, "1.0", "1.0.0.0"), 0)

if __name__ == "__main__":
    unittest.main()