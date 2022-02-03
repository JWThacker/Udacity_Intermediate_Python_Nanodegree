"""Class to parse quotes from a CSV file.

Defines a class to parse quotes from a CSV file. The parse method returns
a list of QuoteModel objects.
"""

import pandas as pd
from typing import List
from .quote_model import QuoteModel

from .ingestor_interface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """Class to parse quotes from a CSV file."""

    allowable_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from a CSV file.

        params:
            path: str - a path to a CSV file (a string).
        returns:
            List[QuoteModels] - a lists of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            ext = path.split('.')[-1]
            raise Exception(f'Cannot ingest a {ext}')

        df = pd.read_csv(path, header=0)
        df['full_quote'] = df['body'] + ' - ' + df['author']
        quotes = [QuoteModel(quote) for quote in df['full_quote']]
        return quotes
