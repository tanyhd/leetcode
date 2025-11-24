import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.prefixesDivBy5(Solution, [0,1,1]), [True,False,False])

    def test_case_2(self):
        self.assertEqual(self.sol.prefixesDivBy5(Solution, [1,1,1]), [False,False,False])


if __name__ == "__main__":
    unittest.main()