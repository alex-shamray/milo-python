import unittest
from dateparser import parse


class TestCase(unittest.TestCase):
    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Y_m_d(self):
        # Test Y/m/d format.
        self.assertEqual(parse('1/2/3'), '2001-02-03')

    def test_m_d_Y(self):
        # Test m/d/Y format.
        self.assertEqual(parse('3/20/1'), '2001-03-20')

    def test_d_m_Y(self):
        # Test d/m/Y format.
        self.assertEqual(parse('3/2/2001'), '2001-02-03')

    def test_wrong_format(self):
        # Test wrong format.
        self.assertEqual(parse('23/33/15'), '23/33/15 is illegal')


if __name__ == '__main__':
    unittest.main()
