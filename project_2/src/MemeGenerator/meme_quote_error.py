"""Defines an exception in case the body of the quote in the meme is empty."""


class MemeQuoteError(Exception):
    """Exception class for quotes.

    Exception class in case the body (or author) of
    quote in the meme is left empty.
    """

    def __init(self, message='Body of meme must not be empty.'):
        self.message = message
        super().__init__(self.message)
