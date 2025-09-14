import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.spellchecker(Solution, ["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]), ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"])

    def test_case_2(self):
        self.assertEqual(self.sol.spellchecker(Solution, ["yellow"], ["YellOw"]), ["yellow"])

if __name__ == "__main__":
    unittest.main()