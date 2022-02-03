import unittest
import os

from .ingestor import Ingestor


class MyTestCase(unittest.TestCase):
    def test_ingestor_text(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src'
                   '/_data/DogQuotes/DogQuotesTXT.txt')
        expected = ('"To bork or not to bork" - Bork\n'
                    '"He who smelt it..." - Stinky')
        my_quotes = Ingestor.parse(my_path)
        actual = ''
        for quote in my_quotes:
            actual += str(quote) + '\n'
        actual = actual.strip()
        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual)

    def test_ingestor_csv(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src'
                   '/_data/DogQuotes/DogQuotesCSV.csv')
        expected = ('"Chase the mailman" - Skittle\n'
                    '"When in doubt, go shoe-shopping" - Mr. Paws')
        my_quotes = Ingestor.parse(my_path)
        actual = ''
        for quote in my_quotes:
            actual += str(quote) + '\n'
        actual = actual.strip()
        self.assertEqual(expected, actual)

    def test_ingestor_pdf(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src'
                   '/_data/DogQuotes/DogQuotesPDF.pdf')
        actual = ''
        quotes = Ingestor.parse(my_path)
        for quote in quotes:
            actual += str(quote) + '\n'
        actual = actual.strip()
        expected = ('"Treat yo self" - Fluffles\n'
                    '"Life is like a box of treats" - Forrest Pup\n'
                    '"It\'s the size of the fight in the dog" - Bark Twain')
        self.assertEqual(expected, actual)
        tmp_dir = './tmp_data'
        self.assertFalse(os.path.exists(tmp_dir))

    def test_ingestor_docx(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src'
                   '/_data/DogQuotes/DogQuotesDOCX.docx')
        dog_quotes = Ingestor.parse(my_path)
        actual = ''
        for quote in dog_quotes:
            actual += str(quote) + '\n'
        actual = actual.strip()
        expected = ('"Bark like no one’s listening" - Rex\n'
                    '"RAWRGWAWGGR" - Chewy\n'
                    '"Life is like peanut butter: crunchy" - Peanut\n'
                    '"Channel your inner husky" - Tiny')
        self.assertEquals(expected, actual)

    def test_ingestor_ext_not_supported(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src'
                   '/_data/DogQuotes/DogQuotes.json')
        dog_quotes = Ingestor.parse(my_path)
        actual = len(dog_quotes)
        expected = 0
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
