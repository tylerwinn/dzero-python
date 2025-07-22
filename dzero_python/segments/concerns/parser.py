"""Parser mixin for segment parsing functionality"""

import re

class ParserMixin:
    """Mixin providing parsing functionality for segments"""
    
    @classmethod
    def parse(cls, source):
        """
        Parse a segment from a string
        
        Args:
            source (str): Raw segment string to parse
            
        Returns:
            Segment instance
        """
        # Split on field/group/segment separators and remove empty elements
        elements = [e for e in re.split(r'[\x1C\x1E\x03\x1D]', source) if e]
        
        # Create hash from field ID (first 2 chars) to value (remaining chars)
        segment_hash = {}
        for element in elements:
            if len(element) >= 2:
                field_id = element[:2]
                field_value = element[2:]
                segment_hash[field_id] = field_value
        
        return cls.build(segment_hash)
