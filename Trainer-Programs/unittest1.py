import unittest

def multiply(a, b):
    """ """
    return a*b
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual( multiply('a',5), 'aaaaa')
		
    def test_strings_not_a_3(self):
        self.assertNotEqual( multiply('a',2), 'aaa')		
 
if __name__ == '__main__':
    unittest.main()