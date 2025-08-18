import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.judgePoint24(Solution, [4,1,8,7]), True)

    def test_case_2(self):
        self.assertEqual(self.sol.judgePoint24(Solution, [1,2,1,2]), False)
    
    def test_case_3(self):
        self.assertEqual(self.sol.judgePoint24(Solution, [8,1,6,6]), True)


if __name__ == "__main__":
    unittest.main()