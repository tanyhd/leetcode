import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.flowerGame(Solution, 3, 2), 3)

    def test_case_2(self):
        self.assertEqual(self.sol.flowerGame(Solution, 1, 1), 0)
    
if __name__ == "__main__":
    unittest.main()