import unittest

from pagination import page


class PaginationTests(unittest.TestCase):
    def test_first_page(self):
        self.assertEqual(page(['a', 'b', 'c'], 1, 2), ['a', 'b'])

    def test_invalid_page(self):
        with self.assertRaises(ValueError):
            page(['a'], 0, 2)


if __name__ == '__main__':
    unittest.main()
