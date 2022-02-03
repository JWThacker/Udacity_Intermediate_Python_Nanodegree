"""Class to store quotes.

This class defines a class to store the quotes that will be used
by the MemeGenerator class.
"""


class QuoteModel:
    """A class to store the quotes for the memes.

    This class defines a class to store the quotes for the memes produced
    by the MemeGenerator class.

    Fields:
        _body(private) - the body of the quote.
        _author (private) - the author of the quote.

    Methods:
        __init__ - the constructor for the QuoteModel class.
        __str__ - prints a string representation for a
                      QuoteModel object.
        author (setter/getter) - overwrites/returns the value from the
                                     _author field.
        body (setter/getter) - overwrites/returns the vlaue from the
                                   _body field.
    """

    def __init__(self, quote: str):
        """Instantiate an instance for the QuoteModel Class.

        Params:
            quote: str - A quote including both the body and the author.
        throws:
            TypeError - if the quote parameter is a string.
        """
        try:
            self._author = quote.split(' - ')[-1]
            self._body = quote.split(' - ')[0].strip('\"')
        except AttributeError:
            raise TypeError('quote must be string.')

    def __str__(self):
        """Print a string representation of the QuoteModel class.

        returns:
            A string that gives information of an instance of QuoteModel.
        """
        return f'"{self._body}" - {self._author}'

    @property
    def author(self):
        """Return the value stored in the _author field.

        returns:
            the values stored in the _author field.
        """
        return self._author

    @author.setter
    def author(self, author):
        """Store a new value in the _author field.

        params:
            author - the new value of _author.
        """
        self._author = author

    @property
    def body(self):
        """Return the value stored in _body field.

        returns:
            the value stored in the _body field.
        """
        return self._body

    @body.setter
    def body(self, body):
        """Store a new value in the _body field.

        params:
            body - the new value of _body.
        """
        self._body = body
