"""Class to parse quotes from a flat text file.

This class defines a method to parse quotes from a flat text file.
The parse method returns a list of QuoteModel objects.
"""

from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class TextIngestor(IngestorInterface):
    """Class to parse quotes from a flat text file."""

    allowable_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of QuoteModel objects.

        params:
            path: str - a path to the flat text file (a string).
        """
        if not cls.can_ingest(path):
            ext = path.split('.')[-1]
            raise Exception(f'Cannot ingest a {ext}')

        quotes = []
        with open(path, mode='r', encoding='utf-8-sig') as file:
            for line in file:
                line = line.strip()
                if line != '':
                    quotes.append(QuoteModel(line))

        return quotes
