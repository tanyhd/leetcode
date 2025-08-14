import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.largestGoodInteger(Solution, "6777133339"), "777")

    def test_case_2(self):
        self.assertEqual(self.sol.largestGoodInteger(Solution, "2300019"), "000")
    
    def test_case_3(self):
        self.assertEqual(self.sol.largestGoodInteger(Solution, "42352338"), "")


if __name__ == "__main__":
    unittest.main()