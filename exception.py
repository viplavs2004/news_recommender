import sys
from logger import logger

class CustomException(Exception):
    """Custom Exception class for detailed error handling."""

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = CustomException.get_detailed_error(error_message, error_detail)

    @staticmethod
    def get_detailed_error(error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error in file [{file_name}] at line [{line_number}] → {error_message}"

    def __str__(self):
        return self.error_message
