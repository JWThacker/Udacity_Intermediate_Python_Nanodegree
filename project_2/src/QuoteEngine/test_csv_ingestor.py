import unittest
from .csv_ingestor import CSVIngestor


class TestCSVIngestor(unittest.TestCase):
    def test_csv_ingestor_typical(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src/'
                   '_data/DogQuotes/DogQuotesCSV.csv')
        expected = ('"Chase the mailman" - Skittle\n'
                    '"When in doubt, go shoe-shopping" - Mr. Paws')
        my_quotes = CSVIngestor.parse(my_path)
        actual = ''
        for quote in my_quotes:
            actual += str(quote) + '\n'
        actual = actual.strip()
        self.assertEqual(expected, actual)

    def test_csv_wrong_ext(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/'
                   'src/_data/DogQuotes/DogQuotesTXT.txt')
        with self.assertRaises(Exception):
            CSVIngestor.parse(my_path)

    def test_csv_empty_path(self):
        with self.assertRaises(TypeError):
            CSVIngestor.parse()


if __name__ == '__main__':
    unittest.main()
