import string

class PalindromeChecker:
    def __init__(self):
        """Initialize the PalindromeChecker."""
        pass

    def clean_input(self, input_string):
        """
        Clean the input string by removing punctuation and spaces,
        and converting it to lowercase.

        Args:
            input_string (str): The string to be cleaned.

        Returns:
            str: The cleaned string.
        """
        # Remove punctuation and convert to lowercase
        cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
        return cleaned_string

    