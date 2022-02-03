import unittest
from QuoteEngine import QuoteModel


class TestQuoteModel(unittest.TestCase):
    def test_quote_model(self):
        my_quote = QuoteModel('"All Dogs go to Heaven" - Someone')
        self.assertEqual('Someone', my_quote.author)
        self.assertEqual('All Dogs go to Heaven', my_quote.body)

    def test_quote_model_type_error(self):
        with self.assertRaises(TypeError):
            my_quote = QuoteModel()
            my_quote = QuoteModel(5)
            my_quote = QuoteModel(sdf)
            my_quote = QuoteModel(10.0)


if __name__ == '__main__':
    unittest.main()
