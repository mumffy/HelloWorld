import unittest
# from HelloWorld import double_it
from HelloWorld import HelloWorld


class HelloWorldTests(unittest.TestCase):
    def test_double_it(self):
        self.assertEqual(HelloWorld.double_it(1), 2)

    def test_double_it_negatives(self):
        self.assertEqual(HelloWorld.double_it(-1), -2)

if __name__ == '__main__':
    unittest.main()
