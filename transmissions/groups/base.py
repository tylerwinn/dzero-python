"""Base class for transmission groups"""

import json

class BaseGroup:
    """Base class for transmission and transaction groups"""
    
    def __init__(self, segments=None):
        """
        Initialize group with segments
        
        Args:
            segments (list): List of segment instances
        """
        self.segments = segments or []
    
    @classmethod
    def parse(cls, string):
        """
        Parse a group from string
        
        Args:
            string (str): Raw group string
            
        Returns:
            Group instance
        """
        # Split string into segments and parse each one
        raw_segments = string.split("\x1E")  # SEGMENT_SEPARATOR
        segments = []
        
        for raw_segment in raw_segments:
            if raw_segment.strip():  # Skip empty segments
                # Import here to avoid circular import
                from ...segments import BaseSegment
                segment = BaseSegment.parse(raw_segment)
                segments.append(segment)
        
        return cls(segments=segments)
    
    def to_s(self):
        """
        Serialize group to string
        
        Returns:
            str: Serialized group
        """
        # Default implementation - subclasses may override
        string = "\x1D"  # GROUP_SEPARATOR
        string += "\x1E"  # SEGMENT_SEPARATOR
        string += "".join(segment.to_s() for segment in self.segments)
        
        # Remove trailing segment separator
        if string.endswith("\x1E"):
            string = string[:-1]
            
        return string
    
    def to_json(self, key_group_by_segment_sym=False, **options):
        """
        Serialize group to JSON/dict
        
        Args:
            key_group_by_segment_sym (bool): Group by segment symbol instead of array
            **options: Additional serialization options
            
        Returns:
            dict: JSON representation
        """
        if key_group_by_segment_sym:
            # Group segments by symbol name
            result = {}
            for segment in self.segments:
                if segment:
                    symbol = segment.__class__.symbol
                    result[symbol] = segment.to_json(**options)
            return result
        else:
            # Return as array of segments
            return {
                "segments": [segment.to_json(**options) for segment in self.segments if segment]
            }
    
    def get_segment(self, segment_class):
        """
        Get first segment of specified class, creating if not found
        
        Args:
            segment_class: Segment class to find
            
        Returns:
            Segment instance
        """
        # Look for existing segment of this class
        for segment in self.segments:
            if isinstance(segment, segment_class):
                return segment
        
        # Create new segment if not found
        new_segment = segment_class()
        self.segments.append(new_segment)
        return new_segment

    def __getattr__(self, name):
        """
        Dynamic segment access via {segment_symbol}_segment attributes
        
        Args:
            name (str): Attribute name
            
        Returns:
            Segment instance or raises AttributeError
        """
        if name.endswith('_segment'):
            segment_symbol = name[:-8]  # Remove '_segment' suffix
            
            # Import here to avoid circular import
            from ...segments import BaseSegment
            
            # Find segment class by symbol
            segment_class = BaseSegment.get_klass_by_symbol(segment_symbol)
            if segment_class and segment_class != BaseSegment:
                return self.get_segment(segment_class)
        
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
