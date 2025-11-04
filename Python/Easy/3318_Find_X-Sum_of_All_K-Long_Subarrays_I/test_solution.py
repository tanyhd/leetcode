import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.findXSum(Solution, [1,1,2,2,3,4,2,3], 6, 2), [6,10,12])

    def test_case_2(self):
        self.assertEqual(self.sol.findXSum(Solution, [3,8,7,8,7,5], 2, 2), [11,15,15,15,12])
        
    def test_case_3(self):
        self.assertEqual(self.sol.findXSum(Solution, [9,2,2], 3, 3), [13])

if __name__ == "__main__":
    unittest.main()