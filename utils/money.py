from decimal import Decimal
from services.constants import OVERPUNCH

def decode_overpunch(value: str) -> Decimal:
    """
    Decode NCPDP overpunch notation to decimal value.
    
    Overpunch notation uses letters to encode the last digit and sign:
    - {, A-I represent positive values (0-9)
    - }, J-R represent negative values (0, -1 to -9)
    
    Args:
        value: String with overpunch notation (e.g., "30{", "87E")
        
    Returns:
        Decimal value with 2 decimal places (e.g., 3.00, 8.75)
    """
    if not value:
        return Decimal("0.00")
    
    # Check if last character is an overpunch character
    last_char = value[-1]
    
    if last_char in OVERPUNCH:
        # Replace last character with the decoded digit
        digit = OVERPUNCH[last_char]
        numeric_str = value[:-1] + str(abs(digit))
        
        # Convert to decimal (values are in cents, so divide by 100)
        amount = Decimal(numeric_str) / 100
        
        # Apply sign for negative values
        if digit < 0:
            amount = -amount
            
        return amount
    else:
        # No overpunch, just convert normally
        return Decimal(value) / 100

def encode_overpunch(amount: Decimal) -> str:
    """
    Encode a decimal amount into NCPDP overpunch notation.
    
    Args:
        amount: Decimal amount to encode (e.g., 98.79, 4.50)
        
    Returns:
        String in overpunch notation (e.g., "0000987I", "0000045{")
    """
    is_negative = amount < 0
    abs_amount = abs(amount)
    
    # Convert to integer cents
    cents = int((abs_amount * 100).to_integral_value())
    
    # Convert to string and pad with leading zeros to at least 7 digits
    cents_str = str(cents).rjust(8, '0')
    
    # Get last digit
    last_digit = int(cents_str[-1])
    
    # Determine overpunch character
    for char, digit in OVERPUNCH.items():
        if digit == ( -last_digit if is_negative else last_digit):
            overpunch_char = char
            break
    
    # Replace last digit with overpunch character
    encoded_str = cents_str[:-1] + overpunch_char
    
    return encoded_str