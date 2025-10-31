import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.getSneakyNumbers(Solution, [0,1,1,0]), [1,0])

    def test_case_2(self):
        self.assertEqual(self.sol.getSneakyNumbers(Solution, [0,3,2,1,3,2]), [3,2])
        
    def test_case_3(self):
        self.assertEqual(self.sol.getSneakyNumbers(Solution, [7,1,5,4,3,4,6,0,9,5,8,2]), [4,5])

if __name__ == "__main__":
    unittest.main()