from decimal import Decimal, ROUND_HALF_UP


def encode_quantity(amount: Decimal, total_length: int = 10, implied_decimals: int = 3) -> str:
    """
    Convert a decimal amount to a zero-padded quantity string with implied decimals.
    
    Args:
        amount: The decimal amount to convert (e.g., 60.000)
        total_length: Total length of the output string (default 10)
        implied_decimals: Number of implied decimal places (default 3)
        
    Returns:
        Zero-padded string representation (e.g., "0000060000" for 60.000)
    """
    multiplier = Decimal(10 ** implied_decimals)
    shifted = int((amount * multiplier).to_integral_value(rounding=ROUND_HALF_UP))
    return str(shifted).zfill(total_length)

def encode_days_supply(days: Decimal, total_length: int = 3) -> str:
    """
    Convert a decimal days value to a zero-padded days supply string.
    
    Args:
        days: The number of days (e.g., 30, 5.5)
        total_length: Total length of the output string (default 3)
        
    Returns:
        Zero-padded string representation (e.g., "030" for 30 days)
    """
    whole_days = int(Decimal(days).to_integral_value(rounding=ROUND_HALF_UP))
    return str(whole_days).zfill(total_length)

def encode_refills(refills: str, total_length: int = 2) -> str:
    """
    Convert a refills string to a zero-padded refills string.
    
    Args:
        refills: The refills count as a string (e.g., "5", "")
        total_length: Total length of the output string (default 2)
        
    Returns:
        Zero-padded string representation (e.g., "05" for 5 refills, "00" for empty)
    """
    refill_count = int(refills) if refills else 0
    return str(refill_count).zfill(total_length)

def decode_quantity(value: str, implied_decimals: int = 3) -> Decimal:
    """
    Convert a zero-padded quantity string with implied decimals to a Decimal.
    
    Args:
        value: The zero-padded string (e.g., "0000060000")
        implied_decimals: Number of implied decimal places (default 3)
        
    Returns:
        Decimal amount (e.g., Decimal("60.000") for "0000060000")
    """
    if not value:
        return Decimal("0")
    divisor = Decimal(10 ** implied_decimals)
    return Decimal(value) / divisor

def decode_days_supply(value: str) -> Decimal:
    """
    Convert a zero-padded days supply string to an integer.
    
    Args:
        value: The zero-padded string (e.g., "030")
        
    Returns:
        Decimal days (e.g., Decimal("30") for "030")
    """
    if not value:
        return Decimal("0")
    return Decimal(value)

def decode_refills(value: str) -> Decimal:
    """
    Convert a zero-padded refills string to an integer.
    
    Args:
        value: The zero-padded string (e.g., "05")
        
    Returns:
        Integer refill count (e.g., 5 for "05")
    """
    if not value:
        return 0
    return int(value)
