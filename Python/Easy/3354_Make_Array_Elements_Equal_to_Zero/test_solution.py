import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.countValidSelections(Solution, [1,0,2,0,3]), 2)

    def test_case_2(self):
        self.assertEqual(self.sol.countValidSelections(Solution, [2,3,4,0,4,1,0]), 0)


if __name__ == "__main__":
    unittest.main()