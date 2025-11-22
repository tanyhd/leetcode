import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.minimumOperations(Solution, [1,2,3,4]), 3)

    def test_case_2(self):
        self.assertEqual(self.sol.minimumOperations(Solution, [3,6,9]), 0)
        
    def test_case_3(self):
        self.assertEqual(self.sol.minimumOperations(Solution, [8]), 1)

if __name__ == "__main__":
    unittest.main()