import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.kLengthApart(Solution, [1,0,0,0,1,0,0,1], 2), True)

    def test_case_2(self):
        self.assertEqual(self.sol.kLengthApart(Solution, [1,0,0,1,0,1], 2), False)

if __name__ == "__main__":
    unittest.main()