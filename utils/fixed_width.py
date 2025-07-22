"""Utility functions for fixed-width field processing"""

def parse_fixed_width(fields, string):
    """
    Parse a fixed-width string according to field definitions
    
    Args:
        fields (dict): Dictionary mapping field names to their sizes
        string (str): Fixed-width string to parse
        
    Returns:
        dict: Parsed fields as key-value pairs
    """
    result = {}
    position = 0
    
    for field_name, size in fields.items():
        if position + size <= len(string):
            value = string[position:position + size].rstrip()
            result[field_name] = value
            position += size
        else:
            result[field_name] = ""
            
    return result

def to_fixed_width(source, schema):
    """
    Convert a dictionary to a fixed-width string according to schema
    
    Args:
        source (dict): Source data dictionary  
        schema (dict): Schema mapping field names to their sizes
        
    Returns:
        str: Fixed-width formatted string
    """
    result = ""
    
    for field, size in schema.items():
        value = source.get(field, "")
        # Left-align and truncate/pad to exact size
        formatted_value = f"{value:<{size}}"[:size]
        result += formatted_value
        
    return result
