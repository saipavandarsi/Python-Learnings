import unittest

def multiply(a,b):
  return a*b

class TestMul(unittest.TestCase):

  def setup(self):
      pass
  def test_numbers_5_6(self):
      self.assertEqual(multiply(5,6),30)
  def test_Strings_a_6(self) :
      self.assertEqual(multiply('a',6),'aaaaaa')
  def test_numbers_2_3(self):
      self.assertAlmostEqual(multiply(2,3),5,delta=1)

if __name__ == '__main__':
  unittest.main()