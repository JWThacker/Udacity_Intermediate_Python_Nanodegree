import unittest
from .docx_ingestor import DocxIngestor


class test_docx_ingestor(unittest.TestCase):
    def test_can_ingest_true(self):
        my_path = ('~/intermediate_python/project_2/'
                   'src/_data/DogQuotes/DogQuotesDOCX.docx')
        self.assertTrue(DocxIngestor.can_ingest(my_path))

    def test_can_ingest_false(self):
        my_path = ('~intermediate_python/project_2/src/'
                   '_data/DogQuotes/DogQuotesCSV.csv')
        self.assertFalse(DocxIngestor.can_ingest(my_path))

    def test_can_ingest_error(self):
        my_path = None
        with self.assertRaises(TypeError):
            DocxIngestor.can_ingest(my_path)

    def test_parse(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src/'
                   '_data/DogQuotes/DogQuotesDOCX.docx')
        dog_quotes = DocxIngestor.parse(my_path)
        actual = ''
        for quote in dog_quotes:
            actual += str(quote) + '\n'
        actual = actual.strip()
        print(actual)
        expected = ('"Bark like no one’s listening" - Rex\n'
                    '"RAWRGWAWGGR" - Chewy\n'
                    '"Life is like peanut butter: crunchy" - Peanut\n'
                    '"Channel your inner husky" - Tiny')
        self.assertEquals(expected, actual)

    def test_parse_wrong_ext(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src/'
                   '_data/DogQuotes/DogQuotesCSV.csv')
        with self.assertRaises(Exception):
            dog_quotes = DocxIngestor.parse(my_path)

    def test_parse_empty_doc(self):
        my_path = ('/Users/jaredthacker/intermediate_python/project_2/src/'
                   '_data/DogQuotes/empty_docx.docx')
        dog_quotes = DocxIngestor.parse(my_path)
        self.assertEquals(0, len(dog_quotes))


if __name__ == '__main__':
    unittest.main()
