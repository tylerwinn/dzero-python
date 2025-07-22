"""Base class for transmissions"""

from ..utils.fixed_width import to_fixed_width, parse_fixed_width
from .concerns import ParserMixin, SerializerMixin, SegmentMethodsMixin
from .groups import TransmissionGroup, TransactionGroup

class BaseTransmission(ParserMixin, SerializerMixin, SegmentMethodsMixin):
    """Base class for NCPDP D.0 transmissions"""
    
    @classmethod
    def header_schema(cls):
        """
        Define header schema for this transmission type
        Override in subclasses
        
        Returns:
            dict: Field name to size mapping
        """
        raise NotImplementedError("Subclasses must define header_schema")
    
    @classmethod
    def parse(cls, string):
        """
        Parse transmission from NCPDP D.0 string
        
        Args:
            string (str): NCPDP D.0 transmission string
            
        Returns:
            Transmission instance
        """
        if not string:
            return cls()
            
        string = string[:]  # Copy string
        
        # Extract header using fixed-width parsing
        header_length = sum(cls.header_schema().values())
        header_data = string[:header_length]
        string = string[header_length:]
        
        header = parse_fixed_width(cls.header_schema(), header_data)
        
        # Skip segment separator if present
        if string.startswith('\x1E'):
            string = string[1:]
        
        # Split by group separator
        raw_groups = string.split('\x1D')
        raw_transmission_group = raw_groups.pop(0) if raw_groups else ""
        
        # Parse transmission group
        transmission_group = TransmissionGroup.parse(raw_transmission_group)
        
        # Parse transaction groups
        transaction_groups = [TransactionGroup.parse(raw_group) for raw_group in raw_groups if raw_group]
        
        return cls(
            header=header,
            transmission_group=transmission_group, 
            transaction_groups=transaction_groups
        )
    
    def __init__(self, header=None, transmission_group=None, transaction_groups=None, segments=None):
        """
        Initialize transmission
        
        Args:
            header (dict): Header fields
            transmission_group (TransmissionGroup): Transmission level segments
            transaction_groups (list): List of transaction groups
            segments (list): Segments to auto-sort into groups
        """
        self.header = header or {}
        self.transmission_group = transmission_group or TransmissionGroup()
        self.transaction_groups = transaction_groups or []
        
        # Auto-sort segments if provided
        if segments:
            self.sort_segments(segments)
    
    def to_s(self):
        """
        Serialize transmission to NCPDP D.0 string
        
        Returns:
            str: Formatted transmission string
        """
        # Build header using fixed-width formatting
        header_fields = {k: self.header.get(k, "") for k in self.header_schema().keys()}
        header_string = to_fixed_width(header_fields, self.header_schema())
        
        # Build full string
        string = header_string
        string += "\x1E"  # SEGMENT_SEPARATOR
        string += self.transmission_group.to_s()
        string += "".join(group.to_s() for group in self.transaction_groups)
        
        return string
