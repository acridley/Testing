import unittest
import test_code

class tests(unittest.TestCase):
    def test_firstPrimeIsTwo(self):
        self.assertEqual(test_code.prime().getPrime(1), 2)
    def test_secondPrimeIsThree(self):
        self.assertEqual(test_code.prime().getPrime(2), 3)