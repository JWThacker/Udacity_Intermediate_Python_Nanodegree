"""Custom exception on the width of an image."""


class WidthError(Exception):
    """Custom exception on the width of an image."""

    def __init__(self,
                 message='Width must be greater than 0 and less than 500'):
        """Instantiate a WidthError object."""
        self.message = message
        super().__init__(self.message)
