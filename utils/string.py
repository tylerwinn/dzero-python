def format(s: str, length: int, trim: bool = True, to_upper: bool = True) -> str:
    """
    Limit a string to a specified length with optional formatting.
    Args:
        s (str): The input string to be processed.
        length (int): The maximum length of the resulting string.
        trim (bool, optional): Whether to strip leading/trailing whitespace. Defaults to True.
        to_upper (bool, optional): Whether to convert the string to uppercase. Defaults to True.
    Returns:
        str: The processed string with the specified length. Returns an empty string if 
             the input is None or length is <= 0. If the string is shorter than the 
             specified length and trim is False, it will be left-padded with spaces.
             If longer, it will be truncated.
    Examples:
        >>> format("hello world", 5)
        'HELLO'
        >>> format("  test  ", 10, trim=True)
        'TEST'
        >>> format("short", 10, trim=False)
        'SHORT     '
    """

    if s is None or length <= 0:
        return ""
    
    if to_upper:
        s = s.upper()

    if trim:
        s = s.strip()

    if len(s) < length and not trim:
        s = s.ljust(length)

    if len(s) > length:
        s = s[:length]

    return s