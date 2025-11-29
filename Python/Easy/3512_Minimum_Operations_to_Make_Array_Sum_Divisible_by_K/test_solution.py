import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.minOperations(Solution, [3,9,7], 5), 4)

    def test_case_2(self):
        self.assertEqual(self.sol.minOperations(Solution, [4,1,3], 4), 0)
    
    def test_case_3(self):
        self.assertEqual(self.sol.minOperations(Solution, [3,2], 6), 5) 


if __name__ == "__main__":
    unittest.main()