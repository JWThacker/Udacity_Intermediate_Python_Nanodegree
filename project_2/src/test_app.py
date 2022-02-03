import unittest
from app import setup


class MyTestCase(unittest.TestCase):

    def test_setup(self):
        quotes, imgs = setup()
        test_quotes = ['"To bork or not to bork" - Bork',
                       '"He who smelt it..." - Stinky',
                       '"Bark like no one’s listening" - Rex',
                       '"RAWRGWAWGGR" - Chewy',
                       '"Life is like peanut butter: crunchy" - Peanut',
                       '"Channel your inner husky" - Tiny',
                       '"Treat yo self" - Fluffles',
                       '"Life is like a box of treats" - Forrest Pup',
                       '"It\'s the size of the fight in the dog" - Bark Twain',
                       '"Chase the mailman" - Skittle',
                       '"When in doubt, go shoe-shopping" - Mr. Paws']
        self.assertEqual(len(quotes), len(test_quotes))
        for i in range(0, len(quotes)):
            self.assertEqual(str(quotes[i]), test_quotes[i])

        test_images = ['./_data/photos/dog/xander_4.jpg',
                       './_data/photos/dog/xander_3.jpg',
                       './_data/photos/dog/xander_2.jpg',
                       './_data/photos/dog/xander_1.jpg']

        self.assertEqual(len(test_images), len(imgs))
        for i in range(0, len(imgs)):
            self.assertEqual(imgs[i], test_images[i])

        for quote in quotes:
            print(quote)


if __name__ == '__main__':
    unittest.main()
