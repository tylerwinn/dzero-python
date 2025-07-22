"""Rejection codes and validation utilities"""

class RejectionCodes:
    """NCPDP rejection codes and descriptions"""
    
    # Common rejection codes - this would be expanded with full NCPDP codes
    CODES = {
        "01": "M/I BIN Number",
        "02": "M/I Cardholder ID", 
        "03": "M/I Group ID",
        "04": "M/I Cardholder Name",
        "05": "M/I Date of Birth",
        # ... Add more rejection codes as needed
    }
    
    @classmethod
    def get_description(cls, code):
        """Get description for a rejection code"""
        return cls.CODES.get(code, f"Unknown rejection code: {code}")
