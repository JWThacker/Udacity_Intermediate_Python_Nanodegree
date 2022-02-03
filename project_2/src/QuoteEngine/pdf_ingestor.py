"""Class to parse quotes from a PDF.

This is a strategy object used to parse the quotes in a pdf
and stores them as an instance of the QuoteModel class.
"""

import os
import subprocess

from .ingestor_interface import IngestorInterface
from typing import List
from .quote_model import QuoteModel
from .text_ingestor import TextIngestor


class PdfIngestor(IngestorInterface):
    """Class to parse quotes from a PDF."""

    allowable_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of QuoteModel instances from a PDF.

        params:
            path: str - a string representing the path for the PDF file.

        return:
            list[QuoteModels] - a list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            file_ext = path.split('.')[-1]
            raise Exception(f'Cannot ingest a .{file_ext}.')

        tmp_dir = './tmp_data'
        os.makedirs(tmp_dir, exist_ok=True)
        tmp_data = './tmp_data/tmp.txt'
        nopgbrk = '-nopgbrk'
        process = subprocess.run(args=['pdftotext', nopgbrk, path, tmp_data],
                                 capture_output=True)
        if len(process.stderr) > 0:
            os.rmdir(tmp_dir)
            raise FileNotFoundError(f'{path} does not exist.')

        quotes = TextIngestor.parse(tmp_data)
        cls.delete_files(tmp_dir, tmp_data)

        return quotes

    @classmethod
    def delete_files(cls, tmp_dir: str, tmp_data: str):
        """Delete unused temporary directorries.

        params:
            tmp_dir: str - the path to the temprorary directory.
            tmp_data: str - the path to the temporary files.
        """
        if os.path.exists(tmp_data):
            os.remove(tmp_data)
        if os.path.exists(tmp_dir):
            os.rmdir(tmp_dir)
