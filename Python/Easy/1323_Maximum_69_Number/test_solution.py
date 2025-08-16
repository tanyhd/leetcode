import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.maximum69Number(Solution, 9669), 9969)

    def test_case_2(self):
        self.assertEqual(self.sol.maximum69Number(Solution, 9996), 9999)

    def test_case_3(self):
        self.assertEqual(self.sol.maximum69Number(Solution, 9999), 9999)


if __name__ == "__main__":
    unittest.main()