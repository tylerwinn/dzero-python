"""Validation utilities for NCPDP messages"""

import re
from datetime import datetime

class Validator:
    """Validation utilities for NCPDP D.0 messages"""
    
    @staticmethod
    def validate_date(date_str, format_str="%Y%m%d"):
        """
        Validate date string format
        
        Args:
            date_str (str): Date string to validate
            format_str (str): Expected date format (default: YYYYMMDD)
            
        Returns:
            bool: True if valid date, False otherwise
        """
        if not date_str:
            return True  # Empty dates are often allowed
            
        try:
            datetime.strptime(date_str, format_str)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_numeric(value, min_length=None, max_length=None):
        """
        Validate numeric field
        
        Args:
            value (str): Value to validate
            min_length (int): Minimum length (optional)
            max_length (int): Maximum length (optional)
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not value:
            return True  # Empty values often allowed
            
        if not value.isdigit():
            return False
            
        if min_length and len(value) < min_length:
            return False
            
        if max_length and len(value) > max_length:
            return False
            
        return True
    
    @staticmethod
    def validate_alphanumeric(value, max_length=None, pattern=None):
        """
        Validate alphanumeric field
        
        Args:
            value (str): Value to validate
            max_length (int): Maximum allowed length
            pattern (str): Regex pattern to match against
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not value:
            return True
            
        if max_length and len(value) > max_length:
            return False
            
        if pattern and not re.match(pattern, value):
            return False
            
        return True
