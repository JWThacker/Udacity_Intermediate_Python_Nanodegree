import os
import random
import argparse

from MemeGenerator import MemeGenerator
from QuoteEngine import Ingestor, QuoteModel


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        #img = path[0]
        img = path
        print(img)

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(f'"{body}" - {author}')

    meme = MemeGenerator('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description='Optional arguments to make a meme')
    parser.add_argument('--body', type=str, default=None,
                        help=('The text in the meme'))
    parser.add_argument('--author', type=str, default=None,
                        help=('The author of the quote n the meme'))
    parser.add_argument('--path', type=str, default=None,
                        help=('Path to the image that will be used for the'
                              ' meme'))
    args = parser.parse_args()
    #quote_body = args.body
    #quote_author = args.author
    #image_path = args.path
    print(generate_meme(args.path, args.body, args.author))
