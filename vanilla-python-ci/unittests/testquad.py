import sys
sys.path.append('../')
from main import calc_square
import unittest


class MyTests(unittest.TestCase):
    
    def setUp(self):
        self.a = 3
        
    def test_square(self):
        b = calc_square(self.a)
        self.assertTrue( b == 9)

if __name__ == '__main__':
    unittest.main()