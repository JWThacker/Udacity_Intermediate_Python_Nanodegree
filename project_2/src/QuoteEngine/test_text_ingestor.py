import unittest
from .text_ingestor import TextIngestor


class TestTextIngestor(unittest.TestCase):
    def test_parse_typical(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src'
                   '/_data/DogQuotes/DogQuotesTXT.txt')
        expected = ('"To bork or not to bork" - Bork\n'
                    '"He who smelt it..." - Stinky')
        my_quotes = TextIngestor.parse(my_path)
        actual = ''
        for quote in my_quotes:
            actual += str(quote) + '\n'
        actual = actual.strip()
        print(actual.split())
        print(expected.split())
        self.assertEqual(expected, actual)

    def test_parse_wrong_file_ext(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src'
                   '/_data/DogQuotes/DogQuotesPDF.pdf')
        with self.assertRaises(Exception):
            TextIngestor.parse(my_path)

    def test_parse_empty_path(self):
        with self.assertRaises(TypeError):
            TextIngestor.parse()


if __name__ == '__main__':
    unittest.main()
