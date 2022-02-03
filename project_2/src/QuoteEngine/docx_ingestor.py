"""Class to parse quotes from a docx.

This class defines methods that can be used to parse quotes from a docx.
"""

from .ingestor_interface import IngestorInterface
from typing import List
from .quote_model import QuoteModel
from docx import Document


class DocxIngestor(IngestorInterface):
    """Class to parse quotes from a docx."""

    allowable_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from a docx.

        params:
            path: str - a path to docx with quotes to parse (a string).
        returns:
            List[QuoteModel] - a list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            file_ext = path.split('.')[-1]
            raise Exception(f'Cannot ingest a .{file_ext}.')

        doc = Document(path)
        quotes = []

        for paragraph in doc.paragraphs:
            if paragraph.text != '':
                quotes.append(QuoteModel(paragraph.text))
        return quotes
