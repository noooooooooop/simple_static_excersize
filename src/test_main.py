import unittest

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999


class TestMain(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
