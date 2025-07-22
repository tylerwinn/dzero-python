"""Constants for NCPDP D.0 messaging"""

class Constants:
    """NCPDP D.0 Constants and field separators"""
    
    # NCPDP D.0 Field separators
    SEGMENT_SEPARATOR = '\x1E'  # Record Separator (RS) - separates segments
    FIELD_SEPARATOR = '\x1C'    # File Separator (FS) - separates fields within a segment  
    GROUP_SEPARATOR = '\x1D'    # Group Separator (GS) - separates transaction groups
    
    # Version information
    VERSION = 'D0'
    
    # Transaction codes
    TRANSACTION_CODES = {
        'B1': 'Billing Request',
        'B2': 'Reversal Request', 
        'E1': 'Eligibility Request',
        'P1': 'Prior Authorization Request'
    }
    
    # Response status codes
    RESPONSE_STATUS = {
        'A': 'Accepted',
        'R': 'Rejected',
        'C': 'Capture'
    }
    
    # Field validation patterns
    PATTERNS = {
        'DATE_CCYYMMDD': r'^\d{8}$',
        'TIME_HHMMSS': r'^\d{6}$',
        'NUMERIC': r'^\d+$',
        'ALPHANUMERIC': r'^[A-Z0-9\s]*$'
    }
