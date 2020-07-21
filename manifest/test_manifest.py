import os
import unittest

from manifest import Manifest


class MyTestCase(unittest.TestCase):
    def test_check_existing_file(self):
        test_input = 'test.yaml'
        with open(test_input, 'w+') as f:
            self.assertTrue(Manifest.check_existent(test_input))

        os.remove(test_input)

    def test_check_no_existing_file(self):
        test_input = 'test.yaml'
        self.assertFalse(Manifest.check_existent(test_input))




if __name__ == '__main__':
    unittest.main()
