import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.triangleNumber(Solution, [2,2,3,4]), 3)

    def test_case_2(self):
        self.assertEqual(self.sol.triangleNumber(Solution, [4,2,3,4]), 4)
    
    def test_case_3(self):
        self.assertEqual(self.sol.triangleNumber(Solution, [48,66,61,46,94,75]), 19)

if __name__ == "__main__":
    unittest.main()