"""Class that uses the csv_ingestor, etc classes to parse a file for quotes.

Uses the strategy objects (inside the "ingestors" class variable)
to parse quotes from a file.
"""

from .pdf_ingestor import PdfIngestor
from .docx_ingestor import DocxIngestor
from .csv_ingestor import CSVIngestor
from .text_ingestor import TextIngestor
from .quote_model import QuoteModel
from typing import List


class Ingestor:
    """Class that uses the strategy objects to parse a file for quotes."""

    ingestors = [PdfIngestor, DocxIngestor, CSVIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file for quotes.

        params:
            path: str - a path to the
        """
        quotes = []
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                quotes = ingestor.parse(path)
                return quotes
        return quotes
