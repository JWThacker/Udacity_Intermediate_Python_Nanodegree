import unittest
import os

from .pdf_ingestor import PdfIngestor


class test_pdf_ingestor(unittest.TestCase):
    def test_parse_true(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src/'
                   '_data/DogQuotes/DogQuotesPDF.pdf')
        actual = ''
        quotes = PdfIngestor.parse(my_path)
        for quote in quotes:
            actual += str(quote) + '\n'
        actual = actual.strip()
        expected = ('"Treat yo self" - Fluffles\n'
                    '"Life is like a box of treats" - Forrest Pup\n'
                    '"It\'s the size of the fight in the dog" - Bark Twain')
        self.assertEqual(expected, actual)
        tmp_dir = './tmp_data'
        self.assertFalse(os.path.exists(tmp_dir))

    def test_parse_two_files(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src/'
                   '_data/DogQuotesDogQuotesPDF.pdf')
        my_second_path = ('/Users/jaredthacker/intermediate_python/project_2/'
                          'src/_data/DogQuotes/more_quotes.pdf')
        actual = ''
        quotes = PdfIngestor.parse(my_path)
        for quote in quotes:
            actual += str(quote) + '\n'
        actual = actual.strip()
        expected = ('"Treat yo self" - Fluffles\n'
                    '"Life is like a box of treats" - Forrest Pup\n'
                    '"It\'s the size of the fight in the dog" - Bark Twain')
        print(expected)
        self.assertEqual(expected, actual)
        expected = ('"Bark like no one’s listening" - Rex\n'
                    '"RAWRGWAWGGR" - Chewy\n'
                    '"Life is like peanut butter: crunchy" - Peanut\n'
                    '"Channel your inner husky" - Tiny')
        quotes = PdfIngestor.parse(my_second_path)
        actual = ''
        for quote in quotes:
            actual += str(quote) + '\n'
        actual = actual.strip()
        self.assertEqual(expected, actual)
        tmp_dir = './tmp_data'
        self.assertFalse(os.path.exists(tmp_dir))

    def test_can_ingest_false(self):
        my_path = ('~/intermediate_python/project_2/src/_data/DogQuotes'
                   'DogQuotesDOCX.docx')
        self.assertFalse(PdfIngestor.can_ingest(my_path))
        tmp_dir = './tmp_data'
        self.assertFalse(os.path.exists(tmp_dir))

    def test_can_ingest_error(self):
        my_path = None
        with self.assertRaises(TypeError):
            PdfIngestor.can_ingest(my_path)
        tmp_dir = './tmp_data'
        self.assertFalse(os.path.exists(tmp_dir))

    def test_parse_file_doesnt_exist(self):
        my_path = ('~/intermediate_python/project_2/src/_data/DogQuotes/'
                   'fake_pdf.pdf')
        with self.assertRaises(FileNotFoundError):
            quotes = PdfIngestor.parse(my_path)
        tmp_dir = './tmp_data'
        self.assertFalse(os.path.exists(tmp_dir))


if __name__ == '__main__':
    unittest.main()
