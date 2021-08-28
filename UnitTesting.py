import unittest
import crawler as prog

class UnitTesting(unittest.TestCase):

    def test_StatusCode(self):
        SCode = prog.Quest5(200)
        self.assertEqual(SCode.StatusCode, 200)

if __name__ == '__main__':
    unittest.main()

