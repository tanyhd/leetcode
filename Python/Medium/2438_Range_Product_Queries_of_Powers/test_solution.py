import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.productQueries(Solution, 15, [[0,1],[2,2],[0,3]]), [2,4,64])

    def test_case_2(self):
        self.assertEqual(self.sol.productQueries(Solution, 2, [[0,0]]), [2])


if __name__ == "__main__":
    unittest.main()