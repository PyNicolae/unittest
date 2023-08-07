from division import divisions
import unittest

class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertRaises(ZeroDivisionError,divisions(1,0))

    def test_division1(self):
        self.assertRaises(TypeError,divisions(1,"2"))

if __name__ == '__main__':
    unittest.main()