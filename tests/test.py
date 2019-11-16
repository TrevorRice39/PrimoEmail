import unittest
import filecmp
import os
import sys
# put our src dir in the system path so we can import main and sort
dir_path = os.getcwd()
dir_path = dir_path[0 : dir_path.rfind('/')] + '/src'
sys.path.append(dir_path)

class Tests(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()