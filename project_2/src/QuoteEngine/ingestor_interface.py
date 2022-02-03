"""Interface for the strategy objects in this module.

Provides an interface for the strategy objects: csv_ingestor,
docx_ingestor, pdf_ingestor and text_ingestor.
"""

from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """Interface for the strategy objects in this module."""

    allowable_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Determine whether this strategy object can parse given file.

        params:
            path: str - a path to the file to be parsed.
        returns:
            a boolean - whether or not the file can be parsed.
        """
        try:
            file_ext = path.split(".")[-1]
            if file_ext not in cls.allowable_extensions:
                return False
            return True
        except AttributeError:
            raise TypeError(f'Path needs to be a string not a {type(path)}.')

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method for parse. See strategy object implementation."""
        pass
