"""This script uses the Ingestor class to generate a random captioned image.

This script generates a captioned image of the user's specification or
a randomly captioned if the user provides no input.

"""

import argparse
import os
import random

from MemeGenerator import MemeGenerator as mg
from QuoteEngine import Ingestor


def main():
    """Ingestor class is used to generate a (possibly random) captioned image.

    Generates a randomly captioned image if no user input is received or
    generates a captioned image (a meme) of the user's choosing if specified
    by the command line arguments below.

    CLI arguments:
        path - a path to an image to write text on.
        body - a quote to be used as the caption of the meme.
        author - the author of the quote (see above).
    """
    parser = argparse.ArgumentParser(description=('Optional arguments to' ''
                                                  'make a meme'))
    parser.add_argument('--body', type=str, default=None,
                        help=('The text in the meme'))
    parser.add_argument('--author', type=str, default=None,
                        help=('The author of the quote n the meme'))
    parser.add_argument('--path', type=str, default=None,
                        help=('Path to the image that will be used for the'
                              ' meme'))
    args = parser.parse_args()
    quote_body = args.body
    quote_author = args.author
    image_path = args.path

    if not image_path:
        photo_directory_names = os.scandir(path='./_data/photos')

        photo_directories = []
        for directory_name in photo_directory_names:
            if not directory_name.name.startswith('.'):
                photo_directories.append(directory_name.name)

        num_dirs = len(photo_directories)
        random_index = random.randint(0, num_dirs - 1)
        random_dir = photo_directories[random_index]

        photo_names = os.scandir(path='./_data/photos/' + random_dir)
        photos = []
        for photo_name in photo_names:
            photos.append(photo_name.name)

        num_photos = len(photos)
        random_index = random.randint(0, num_photos - 1)
        random_photo_name = photos[random_index]
        random_photo_path = './_data/photos' + '/'\
                            + random_dir + '/' + random_photo_name
        image_path = random_photo_path
        print(random_photo_path)

    if not quote_body:
        dog_quotes_file_names = os.scandir(path='./_data/DogQuotes')

        dog_quotes_files = []
        for dog_quotes_file_name in dog_quotes_file_names:
            if not dog_quotes_file_name.name.startswith('.'):
                dog_quotes_files.append(dog_quotes_file_name.name)

        num_files = len(dog_quotes_files)
        random_index = random.randint(0, num_files - 1)
        random_file = dog_quotes_files[random_index]

        quote_objs = Ingestor.parse('./_data/DogQuotes/' + random_file)

        num_quotes = len(quote_objs)
        random_index = random.randint(0, num_quotes - 1)
        random_quote = quote_objs[random_index]
        quote_body = random_quote.body
        quote_author = random_quote.author
    else:
        if not quote_author:
            raise Exception('Quote must have an author')

    # After MemeGenerator is fixed edit the below path to only
    # be the directory to where you want the meme saved.
    meme = mg('./tmp')
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    meme_path = meme.make_meme(image_path, quote_body, quote_author)
    print(meme_path)


if __name__ == '__main__':
    main()
