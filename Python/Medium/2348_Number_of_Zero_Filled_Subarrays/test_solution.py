import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.zeroFilledSubarray(Solution, [1,3,0,0,2,0,0,4]), 6)

    def test_case_2(self):
        self.assertEqual(self.sol.zeroFilledSubarray(Solution, [0,0,0,2,0,0]), 9)
    
    def test_case_3(self):
        self.assertEqual(self.sol.zeroFilledSubarray(Solution, [2,10,2019]), 0)

if __name__ == "__main__":
    unittest.main()