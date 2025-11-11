import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.findMaxForm(Solution, ["10","0001","111001","1","0"], 5, 3), 4)

    def test_case_2(self):
        self.assertEqual(self.sol.findMaxForm(Solution, ["10","0","1"], 1, 1), 2)
    
    def test_case_3(self):
        self.assertEqual(self.sol.findMaxForm(Solution, ["10","0001","111001","1","0"], 4, 3), 3)

    def test_case_4(self):
        self.assertEqual(self.sol.findMaxForm(Solution, ["00","000"], 1, 10), 0)

if __name__ == "__main__":
    unittest.main()