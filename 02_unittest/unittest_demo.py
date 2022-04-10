#http://puremonkey2010.blogspot.com/2017/08/python-mock-python-unit-test.html

from util import func1,func2
import unittest
from unittest import mock

class ExampleTest(unittest.TestCase):
    def test_func2(self):
        self.assertEqual(func2(5), 50)
class Func2Test(unittest.TestCase):
    @mock.patch('util.func1')
    def test_func2(self, mock_func1):
        mock_func1.return_value = 0
        self.assertEqual(func2(5), 25)

if __name__ == '__main__':
    unittest.main()

#coverage
# coverage run unittest_demo.py
# coverage run -m unittest_demo
# coverage report 
#C:\Users\qoojo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts