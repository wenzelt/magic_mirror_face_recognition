# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class FaceMatchNotFound(Error):
    """Raised when the input value is too small"""

    pass


class DatabaseEmptyException(Exception):
    """Raised when database is empty"""

    pass
