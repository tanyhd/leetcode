import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.numberOfPaths(Solution, [[5,2,4],[3,0,5],[0,7,2]], 3), 2)

    def test_case_2(self):
        self.assertEqual(self.sol.numberOfPaths(Solution, [[0,0]], 5), 1)
    
    def test_case_3(self):
        self.assertEqual(self.sol.numberOfPaths(Solution, [[7,3,4,9],[2,3,6,2],[2,3,7,0]], 1), 10)

    def test_case_4(self):
        self.assertEqual(self.sol.numberOfPaths(Solution, [[1,5,3,7,3,2,3,5]], 29), 1)


if __name__ == "__main__":
    unittest.main()