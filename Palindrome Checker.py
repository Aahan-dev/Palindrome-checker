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

    def is_palindrome(self, input_string):
        """
        Check if the cleaned input string is a palindrome.


        Args:
            input_string (str): The string to check.


        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        cleaned_string = self.clean_input(input_string)
        # Check if the string reads the same forwards and backwards
        return cleaned_string == cleaned_string[::-1]


    def run(self):
        """Run the palindrome checker tool."""
        while True:
            user_input = input("Enter a word or phrase (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the palindrome checker. Goodbye!")
                break
           
            if self.is_palindrome(user_input):
                print(f'"{user_input}" is a palindrome.')
            else:
                print(f'"{user_input}" is not a palindrome.')


if __name__ == "__main__":
    # Create an instance of PalindromeChecker and run it
    checker = PalindromeChecker()
    checker.run()
