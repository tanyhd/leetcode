import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.replaceNonCoprimes(Solution, [6,4,3,2,7,6,2]), [12,7,6])

    def test_case_2(self):
        self.assertEqual(self.sol.replaceNonCoprimes(Solution, [2,2,1,1,3,3,3]), [2,1,1,3])


if __name__ == "__main__":
    unittest.main()