import unittest

from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.isValid(Solution, "()"), True)

    def test_case_2(self):
        self.assertEqual(self.sol.isValid(Solution, "()[]{}"), True)

    def test_case_3(self):
        self.assertEqual(self.sol.isValid(Solution, "(]"), False)
    
    def test_case_4(self):
        self.assertEqual(self.sol.isValid(Solution, "([])"), True)
    
    def test_case_5(self):
        self.assertEqual(self.sol.isValid(Solution, "([)]"), False)


if __name__ == "__main__":
    unittest.main()