import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.findSmallestInteger(Solution, [1,-10,7,13,6,8], 5), 4)

    def test_case_2(self):
        self.assertEqual(self.sol.findSmallestInteger(Solution, [1,-10,7,13,6,8], 7), 2)

    def test_case_3(self):
        self.assertEqual(self.sol.findSmallestInteger(Solution, [3,0,3,2,4,2,1,1,0,4], 5), 10)

    def test_case_4(self):
        self.assertEqual(self.sol.findSmallestInteger(Solution, [0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1], 2), 15)


if __name__ == "__main__":
    unittest.main()