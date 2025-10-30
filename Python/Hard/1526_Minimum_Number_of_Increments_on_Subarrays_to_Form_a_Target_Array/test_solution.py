import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.minNumberOperations(Solution, [1,2,3,2,1]), 3)

    def test_case_2(self):
        self.assertEqual(self.sol.minNumberOperations(Solution, [3,1,1,2]), 4)

    def test_case_3(self):
        self.assertEqual(self.sol.minNumberOperations(Solution, [3,1,5,4,2]), 7)


if __name__ == "__main__":
    unittest.main()