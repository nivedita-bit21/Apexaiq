import re

class CreditCardValidator:
    """
    A class to validate credit card numbers based on ABCD Bank's specifications.

    Validation Rules:
    1. Must start with 4, 5, or 6.
    2. Must be exactly 16 digits.
    3. Can be divided into groups of 4 separated by hyphens.
    4. Must not contain any other separators.
    5. Must not have 4 or more consecutive repeated digits.
    6. Must pass the Luhn algorithm check.
    """

    def __init__(self):
        # Compile regex patterns for better performance
        self.structure_pattern = re.compile(
            r'^[4-6]\d{3}(-?\d{4}){3}$'
        )
        self.consecutive_pattern = re.compile(r'(\d)\1{3}')

    def validate(self, card_number: str) -> bool:
        """
        Main validation method that combines all checks.

        Args:
            card_number (str): The credit card number to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return all([
            self._check_structure(card_number),
            self._check_consecutive_digits(card_number),
            self._luhn_check(card_number)
        ])

    def _check_structure(self, card_number: str) -> bool:
        """
        Validates the basic structure of the credit card number.

        Args:
            card_number (str): The credit card number to validate.

        Returns:
            bool: True if structure is valid, False otherwise.
        """
        return bool(self.structure_pattern.match(card_number))

    def _check_consecutive_digits(self, card_number: str) -> bool:
        """
        Checks for 4 or more consecutive repeated digits.

        Args:
            card_number (str): The credit card number to validate.

        Returns:
            bool: False if invalid consecutive digits found, True otherwise.
        """
        # Remove hyphens and check for consecutive digits
        clean_number = card_number.replace('-', '')
        return not bool(self.consecutive_pattern.search(clean_number))

    def _luhn_check(self, card_number: str) -> bool:
        """
        Validates the credit card number using the Luhn algorithm.

        Args:
            card_number (str): The credit card number to validate.

        Returns:
            bool: True if the card number is valid per Luhn algorithm, False otherwise.
        """
        # Remove hyphens
        clean_number = card_number.replace('-', '')
        digits = [int(d) for d in clean_number]
        checksum = 0

        # Reverse the digits for processing
        digits.reverse()

        for i, digit in enumerate(digits):
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit

        return checksum % 10 == 0

def main():
    """
    Main function to handle input/output and process validation.
    """
    n = int(input("Enter the number of credit card numbers to validate: "))
    validator = CreditCardValidator()

    for _ in range(n):
        card = input("Enter credit card number: ").strip()
        if validator.validate(card):
            print("Valid")
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
