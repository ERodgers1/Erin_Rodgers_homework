from util import C_to_F
from util import F_to_C
import unittest

class unitTest(unittest.TestCase):
    def test_C_to_F(self):
        self.assertRaises(ValueError, C_to_F, -100)

    def test_F_to_C(self):
        self.assertRaises(ValueError, F_to_C, -45)

    def test_C_to_F_temp(self):
       temp_test = C_to_F(-50)
       self.assertEqual(temp_test, -55.9 )

    def test_F_to_C_temp(self):
       temp_test = F_to_C(-76)
       self.assertEqual(temp_test, -79.5)

unittest.main()
