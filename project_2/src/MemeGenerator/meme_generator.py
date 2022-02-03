"""Class to generate a meme from a quote, output path and an image."""


import random
import textwrap

from PIL import Image, ImageDraw, ImageFont
from .width_error import WidthError
from .meme_quote_error import MemeQuoteError


class MemeGenerator:
    """Class to generate a meme from a quote, output path and an image."""

    def __init__(self, out_path):
        """Instantiate a MemeGenerator object.

        params:
            out_path - directory where the meme will be saved.
        """
        self._out_path = out_path

    @staticmethod
    def load(in_path) -> Image:
        """Load an image.

        params:
            in_path - the path to the image.
        returns:
            an Image object (as defined by the Pillow package).
        """
        return Image.open(in_path)

    @staticmethod
    def resize(img, width=500) -> Image:
        """Resize an image.

        params:
            img - an Image object (as defined by the Pillow package)
        returns:
            img - a resized Image object.
        """
        if width > 0 and width <= 500:
            width_index = 0
            height_index = 1
            img_width = img.size[width_index]
            img_height = img.size[height_index]
            ratio = width / img_width
            new_height = int(ratio * img_height)
            img = img.resize((width, new_height))
        else:
            raise WidthError

        return img

    @staticmethod
    def add_caption(img: Image, text=None, author=None) -> Image:
        """Add a caption to an image.

        params:
            img: Image - an Image object.
            text - the text in the caption on the image.
            author - the author of the text.
        returns:
            img - an Image object with the caption included.
        """
        if (text is None) or (author is None):
            raise MemeQuoteError()

        lines = textwrap.wrap('"' + text + '"' + ' - ' + author, width=15)
        quote = ''
        for line in lines:
            quote += line + '\n'
        quote.strip()
        font_path = './fonts/arial.ttf'
        width_index = 0
        height_index = 1
        width = img.size[width_index]
        height = img.size[height_index]

        font = ImageFont.truetype(str(font_path), size=30)
        draw = ImageDraw.Draw(img)
        quote_width, quote_height = draw.textsize(str(quote), font=font)
        random_width = random.randint(0, width)
        while random_width + quote_width > width:
            random_width = random.randint(0, width)
        random_height = random.randint(0, height)
        while random_height + quote_height > height:
            random_height = random.randint(0, height)
        draw.text((random_width, random_height), quote,
                  fill=(0, 0, 0), font=font)

        return img

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make a meme of a certain size, with a certain caption etc.

        params:
            img_path - the path to the image to edit.
            text - the text to put in the caption of the meme.
            author - the author of the text.
            width - the width of the new image.
        returns:
            path - the path to the newly made meme.
        """
        img = MemeGenerator.load(img_path)
        res_img = MemeGenerator.resize(img, width)
        cap_img = MemeGenerator.add_caption(res_img, text, author)
        # Have _out_path be the directory and have this method make that
        # directory. Then, .save() save to self._out_path + 'meme.png'.
        path = self._out_path + '/meme.png'
        cap_img.save(path)

        return path

    @property
    def out_path(self):
        """Getter method for the _out_path field."""
        return self._out_path

    @out_path.setter
    def out_path(self, out_path: str):
        self._out_path = out_path

    @property
    def in_path(self):
        """Getter method for the _in_path field."""
        return self._in_path

    @in_path.setter
    def in_path(self, in_path):
        self._in_path = in_path
