import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.finalValueAfterOperations(Solution, ["--X","X++","X++"]), 1)

    def test_case_2(self):
        self.assertEqual(self.sol.finalValueAfterOperations(Solution, ["++X","++X","X++"]), 3)
    
    def test_case_3(self):
        self.assertEqual(self.sol.finalValueAfterOperations(Solution, ["X++","++X","--X","X--"]), 0)


if __name__ == "__main__":
    unittest.main()