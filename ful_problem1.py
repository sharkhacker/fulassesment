import re

def is_valid_contact_number(number):
    # Regular expression pattern for valid contact numbers
    pattern = r'^\+?\d{1,3}[-.\s]?\d{1,3}[-.\s]?\d{3}[-.\s]?\d{4}$'
    
    # Match the pattern 
    if re.match(pattern, number):
        return True
    else:
        return False

# Data Given
contact_numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

# Check validity
for number in contact_numbers:
    if is_valid_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")
