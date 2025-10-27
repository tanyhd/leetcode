import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.numberOfBeams(Solution, ["011001","000000","010100","001000"]), 8)

    def test_case_2(self):
        self.assertEqual(self.sol.numberOfBeams(Solution, ["000","111","000"]), 0)

if __name__ == "__main__":
    unittest.main()