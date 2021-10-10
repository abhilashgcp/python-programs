import sys
import unittest

#Added to run it from the tests folder
sys.path.append('..')
from BackSpace.BackSpaceString import backSpaceString as backSpaceString

#Testcase for the BackSpaceString Program
class BackSpaceString(unittest.TestCase):

    def test_001(self):
        self.assertEqual(backSpaceString("#ab#cd", "#ad#cd" ), True, "Should be True")

    def test_002(self):
        self.assertEqual(backSpaceString("#", "#" ), True, "Should be True")

    def test_003(self):
        self.assertEqual(backSpaceString("#ab#cd", "#ad#ed" ), False, "Should be True")


if __name__ == '__main__':
    unittest.main()