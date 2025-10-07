import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution

    def test_case_1(self):
        self.assertEqual(self.sol.avoidFlood(Solution, [1,2,3,4]), [-1,-1,-1,-1])

    def test_case_2(self):
        self.assertEqual(self.sol.avoidFlood(Solution, [1,2,0,0,2,1]), [-1,-1,2,1,-1,-1])

    def test_case_3(self):
        self.assertEqual(self.sol.avoidFlood(Solution, [1,2,0,1,2]), [])

    def test_case_4(self):
        self.assertEqual(self.sol.avoidFlood(Solution, [69,0,0,0,69]), [-1,69,1,1,-1])

    def test_case_5(self):
        self.assertEqual(self.sol.avoidFlood(Solution, [0,1,1]), [])

    def test_case_6(self):
        self.assertEqual(self.sol.avoidFlood(Solution, [1,0,2,0,2,1]), [-1,1,-1,2,-1,-1])

    def test_case_7(self):
        self.assertEqual(self.sol.avoidFlood(Solution, [1,0,2,0,3,0,2,0,0,0,1,2,3]), [-1,1,-1,2,-1,3,-1,2,1,1,-1,-1,-1])


if __name__ == "__main__":
    unittest.main()